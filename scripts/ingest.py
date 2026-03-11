"""
ingest.py – Pipeline nạp dữ liệu vào ChromaDB
Đọc tài liệu từ data/raw → parse → embedding → lưu vào ChromaDB
"""

import os
import sys

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv(override=True)
import time

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from scripts.parse_docs import parse_all_documents


# ── Cấu hình ──────────────────────────────────────────────
EMBEDDING_MODEL = "models/gemini-embedding-001"
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "knowledge_base", "chroma_db")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
COLLECTION_NAME = "medical_protocols_vn"


def create_embeddings():
    """Khởi tạo embedding model."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            task_type="retrieval_document"
        )
        print(f"✅ Embedding model: {EMBEDDING_MODEL}")
        return embeddings
    except Exception as e:
        print(f"⚠️ Lỗi với {EMBEDDING_MODEL}, chuyển sang gemini-embedding-001...")
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            task_type="retrieval_document"
        )
        print(f"✅ Embedding model fallback: gemini-embedding-001")
        return embeddings


def ingest_documents():
    """Pipeline chính: parse tài liệu → tạo embedding → lưu ChromaDB."""
    
    # 1. Parse tài liệu
    print("📂 Bắt đầu parse tài liệu...")
    data_dir = os.path.abspath(DATA_DIR)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        print(f"⚠️ Thư mục {data_dir} trống. Hãy đặt file PDF/DOCX vào thư mục data/raw/")
        return
    
    chunks = parse_all_documents(data_dir)
    if not chunks:
        print("⚠️ Không tìm thấy tài liệu nào. Hãy đặt file vào data/raw/tim_mach, data/raw/ho_hap, data/raw/noi_tiet")
        return
    
    # 2. Chuyển đổi thành LangChain Documents
    print("\n📝 Chuyển đổi thành Documents...")
    documents = []
    for chunk in chunks:
        doc = Document(
            page_content=chunk['content'],
            metadata=chunk['metadata']
        )
        documents.append(doc)
    
    print(f"   Tổng cộng: {len(documents)} documents")
    
    # 3. Tạo embeddings và lưu vào ChromaDB
    print("\n🔄 Tạo embeddings và lưu vào ChromaDB...")
    embeddings = create_embeddings()
    chroma_dir = os.path.abspath(CHROMA_DIR)
    os.makedirs(chroma_dir, exist_ok=True)
    
    # Khởi tạo (hoặc load) VectorStore từ đầu để có thể ghi đè/append trực tiếp
    batch_size = 10
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=chroma_dir,
        collection_name=COLLECTION_NAME
    )
    
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(documents) + batch_size - 1) // batch_size
        
        print(f"\n   Batch {batch_num}/{total_batches}: Đang xử lý {len(batch)} documents...")
        
        try:
            # Add thẳng vào db, thư viện langchain_chroma mới sẽ tự động lưu xuống ổ cứng
            vectorstore.add_documents(batch)
            print(f"   💾 Đã NHÚNG và LƯU batch {batch_num} thẳng vào ổ cứng (ChromaDB)!")
                
            # Nghỉ 40 giây giữa các batch để tránh bị chặn 429 Quota Exceeded (Free Tier)
            if i + batch_size < len(documents):
                print("   ⏳ Chờ 40s cho API kịp reset giới hạn...")
                time.sleep(40)
                
        except Exception as e:
            print(f"   ❌ Lỗi ở Batch {batch_num}: {e}")
            print("   ⏳ API bị chặn. Nghỉ mệt 60s rồi cứng đầu đâm block này tiếp...")
            time.sleep(60)
            # Thử lại
            vectorstore.add_documents(batch)
            print(f"   💾 (Thử lại) Đã lưu batch {batch_num} vào ổ cứng!")
    
    print(f"\n✅ Đã nạp thành công {len(documents)} chunks vào ChromaDB!")
    print(f"   Đường dẫn: {chroma_dir}")
    print(f"   Collection: {COLLECTION_NAME}")
    
    # 4. Kiểm tra nhanh
    print("\n🔍 Kiểm tra nhanh...")
    test_query = "triệu chứng suy tim"
    results = vectorstore.similarity_search(test_query, k=3)
    print(f"   Query: '{test_query}'")
    print(f"   Kết quả: {len(results)} documents")
    for i, doc in enumerate(results):
        print(f"   [{i+1}] {doc.metadata.get('source', 'N/A')} | {doc.page_content[:100]}...")
    
    return vectorstore


if __name__ == "__main__":
    ingest_documents()
