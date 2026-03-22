"""
rag_engine.py – LangChain RAG Retriever
Hybrid search: ChromaDB (vector) + BM25 (keyword)
Custom ensemble implementation (không dùng EnsembleRetriever deprecated)
"""

import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document


# ── Cấu hình ──────────────────────────────────────────────
EMBEDDING_MODEL = "models/gemini-embedding-001"
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "knowledge_base", "chroma_db")
COLLECTION_NAME = "medical_protocols_vn"


def _create_embeddings():
    """Khởi tạo embedding model với fallback."""
    try:
        return GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            task_type="retrieval_query"
        )
    except Exception as e:
        print(f"⚠️ Warning: Embedding init error, fallback to gemini-embedding-exp: {e}")
        return GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001", 
            task_type="retrieval_query"
        )


_VECTORSTORE_CACHE = None

def load_vectorstore() -> Chroma:
    """Load ChromaDB vectorstore đã có sẵn (có sử dụng memory cache)."""
    global _VECTORSTORE_CACHE
    if _VECTORSTORE_CACHE is not None:
        return _VECTORSTORE_CACHE
        
    embeddings = _create_embeddings()
    chroma_dir = os.path.abspath(CHROMA_DIR)
    
    vectorstore = Chroma(
        persist_directory=chroma_dir,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )
    _VECTORSTORE_CACHE = vectorstore
    return vectorstore


def _deduplicate_docs(docs: list[Document]) -> list[Document]:
    """Loại bỏ documents trùng lặp dựa trên page_content."""
    seen = set()
    unique = []
    for doc in docs:
        content_hash = hash(doc.page_content)
        if content_hash not in seen:
            seen.add(content_hash)
            unique.append(doc)
    return unique


# ── Caching ──────────────────────────────────────────────
_BM25_RETRIEVERS_CACHE = {}

def get_bm25_retriever(vectorstore: Chroma, specialty_filter: str = None) -> BM25Retriever:
    """Lấy BM25 Retriever từ cache hoặc tạo mới nếu chưa có."""
    cache_key = specialty_filter if specialty_filter else "all"
    
    if cache_key in _BM25_RETRIEVERS_CACHE:
        return _BM25_RETRIEVERS_CACHE[cache_key]
        
    bm25_docs = []
    try:
        all_docs_data = vectorstore.get(include=["documents", "metadatas"])
        
        if all_docs_data["documents"]:
            for doc_text, meta in zip(all_docs_data["documents"], all_docs_data["metadatas"]):
                if specialty_filter and meta.get("specialty") != specialty_filter:
                    continue
                bm25_docs.append(Document(page_content=doc_text, metadata=meta))
            
            if bm25_docs:
                bm25_retriever = BM25Retriever.from_documents(bm25_docs, k=5)  # K sẽ được override lúc invoke
                _BM25_RETRIEVERS_CACHE[cache_key] = bm25_retriever
                return bm25_retriever
    except Exception as e:
        print(f"⚠️ BM25 initialization error: {e}")
        
    return None

def hybrid_retrieve(
    query: str,
    vectorstore: Chroma,
    k: int = 5,
    specialty_filter: str = None
) -> list[Document]:
    """
    Tìm kiếm kết hợp: Vector Search + BM25 Keyword Search.
    Lấy kết quả từ cả 2 phương pháp rồi merge và dedup.
    
    Args:
        query: Câu hỏi / triệu chứng
        vectorstore: ChromaDB vectorstore
        k: Số kết quả mỗi phương pháp
        specialty_filter: Lọc chuyên khoa (tùy chọn)
    """
    # 1. Vector Search
    search_kwargs = {"k": k}
    if specialty_filter:
        search_kwargs["filter"] = {"specialty": specialty_filter}
    
    vector_results = []
    try:
        # Lấy distance score từ vectorstore
        score_results = vectorstore.similarity_search_with_score(query, **search_kwargs)
        for doc, distance in score_results:
            # Chroma mặc định trả về L2 squared distance. 
            # Giả định embedding chuẩn hóa, max = 2.0. Chuyển đổi thành %: similarity = 1 - (distance/2)
            sim_pct = round(max(0.0, 1.0 - (distance / 2.0)) * 100, 1)
            doc.metadata["score"] = sim_pct
            vector_results.append(doc)
    except Exception as e:
        print(f"⚠️ Vector search lỗi, chuyển sang fallback: {e}")
        vector_retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs=search_kwargs
        )
        vector_results = vector_retriever.invoke(query)
    
    # 2. BM25 Keyword Search (Sử dụng Cache)
    bm25_results = []
    bm25_retriever = get_bm25_retriever(vectorstore, specialty_filter)
    
    if bm25_retriever:
        try:
            bm25_retriever.k = k # Cập nhật k cho truy vấn hiện tại
            bm25_results = bm25_retriever.invoke(query)
        except Exception as e:
            print(f"⚠️ BM25 search lỗi (tiếp tục với vector search): {e}")
    
    # 3. Merge: vector results first, then BM25 results
    merged = vector_results + bm25_results
    unique_results = _deduplicate_docs(merged)
    
    return unique_results[:k]


def retrieve_context(
    query: str,
    specialty: str = None,
    k: int = 5
) -> list[Document]:
    """
    Truy vấn tri thức y tế từ ChromaDB.
    
    Args:
        query: Câu hỏi / triệu chứng bệnh nhân
        specialty: Chuyên khoa cần lọc
        k: Số kết quả trả về
    
    Returns:
        Danh sách Documents liên quan
    """
    vectorstore = load_vectorstore()
    results = hybrid_retrieve(
        query=query,
        vectorstore=vectorstore,
        k=k,
        specialty_filter=specialty
    )
    return results


def format_context(documents: list[Document]) -> str:
    """
    Format danh sách documents thành chuỗi context cho prompt.
    Bao gồm trích dẫn nguồn.
    """
    if not documents:
        return "Không tìm thấy tài liệu y tế liên quan."
    
    context_parts = []
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get('source', 'Không rõ')
        specialty = doc.metadata.get('specialty', 'Chung')
        score = doc.metadata.get('score', 'N/A')
        
        score_info = f" | Tin cậy: {score}%" if isinstance(score, float) else f" | Nguồn: {score}" if score != 'N/A' else ""
        context_parts.append(
            f"[Nguồn {i}: {source} | Chuyên khoa: {specialty}{score_info}]\n{doc.page_content}"
        )
    
    return "\n\n---\n\n".join(context_parts)
