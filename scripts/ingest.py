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
from scripts.parse_docs import parse_all_documents, parse_document
import argparse


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


def ingest_documents(target_file=None):
    """Pipeline chính: parse tài liệu → tạo embedding → lưu ChromaDB.
    
    Args:
        target_file: Đường dẫn tới 1 file cụ thể (nếu None sẽ quét toàn bộ thư mục DATA_DIR)
    """
    
    # 1. Parse tài liệu
    if target_file:
        if not os.path.exists(target_file):
            print(f"❌ Lỗi: File không tồn tại: {target_file}")
            return
        print(f"📂 Chỉ xử lý file đơn lẻ: {target_file}")
        chunks = parse_document(target_file)
    else:
        data_dir = os.path.abspath(DATA_DIR)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
            print(f"⚠️ Thư mục {data_dir} trống. Hãy đặt file PDF/DOCX vào thư mục data/raw/")
            return
        chunks = parse_all_documents(data_dir)
        
    if not chunks:
        print("⚠️ Không có dữ liệu để nạp.")
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
    batch_size = 20  # Giảm batch size để tránh timeout và quota limit cho Key Free
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=chroma_dir,
        collection_name=COLLECTION_NAME
    )
    
    # 2.5 Lọc các file đã có trong DB (Incremental Ingest) để tiết kiệm Quota
    print("\n🔍 Kiểm tra dữ liệu cũ trong Database...")
    try:
        existing_data = vectorstore.get()
        existing_texts = set()
        
        if existing_data and 'documents' in existing_data and existing_data['documents']:
            existing_texts = set(existing_data['documents'])
            print(f"   Tìm thấy {len(existing_texts)} chunks đã được nạp trước đó.")
            
            # Lọc danh sách documents: chỉ giữ lại những mảnh (chunk) chưa có nội dung trong DB
            new_documents = [doc for doc in documents if doc.page_content not in existing_texts]
            
            skipped_count = len(documents) - len(new_documents)
            if skipped_count > 0:
                print(f"   ⚡ BỎ QUA {skipped_count} chunks vì đã tồn tại trong DB (Tiết kiệm Quota API).")
                documents = new_documents
            else:
                print("   🆕 Tất cả data là mới, tiến hành nạp toàn bộ.")
        else:
            print("   🆕 Database trống hoặc không tìm thấy chunks cũ, nạp toàn bộ.")
            
    except Exception as e:
        print(f"   ⚠️ Lỗi khi kiểm tra DB cũ (có thể DB chưa có hoặc format cũ): {e}")
        print("   Tiến hành nạp thông thường...")

    if not documents:
        print("\n✅ Không có dữ liệu mới nào cần nạp thêm. Tuyệt vời!")
        return vectorstore
    
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(documents) + batch_size - 1) // batch_size
        
        print(f"\n   Batch {batch_num}/{total_batches}: Đang xử lý {len(batch)} documents...")
        
        try:
            # Add thẳng vào db
            vectorstore.add_documents(batch)
            print(f"   💾 Đã NHÚNG và LƯU batch {batch_num}!")
                
            # Nghỉ giữa các batch để tránh bị chặn 429 Quota Exceeded (Free Tier)
            if i + batch_size < len(documents):
                print("   ⏳ Chờ 30s cho API kịp reset giới hạn (Hệ thống bảo vệ Key Free)...")
                time.sleep(30)
                
        except Exception as e:
            print(f"   ❌ Lỗi ở Batch {batch_num}: {e}")
            print("   ⏳ API bị chặn. Nghỉ mệt 60s rồi thử lại...")
            time.sleep(60)
            vectorstore.add_documents(batch)
            print(f"   💾 (Thử lại) Đã lưu batch {batch_num}!")
    
    print(f"\n✅ Đã nạp thành công {len(documents)} chunks vào ChromaDB!")
    print(f"   Đường dẫn: {chroma_dir}")
    print(f"   Collection: {COLLECTION_NAME}")
    
    # 4. Kiểm tra nhanh đa chuyên khoa
    print("\n🔍 Kiểm tra đa chuyên khoa...")
    test_queries = [
        ("Tim mạch", "triệu chứng điển hình suy tim"),
        ("Hô hấp", "tiêu chuẩn chẩn đoán COPD"),
        ("Nội tiết", "biểu hiện của đái tháo đường")
    ]
    
    for spec, query in test_queries:
        results = vectorstore.similarity_search(query, k=2)
        print(f"\n   [Chuyên khoa {spec}] Query: '{query}'")
        if not results:
            print("     ⚠️ Không tìm thấy kết quả.")
        for i, doc in enumerate(results):
            source = doc.metadata.get('source', 'N/A')
            spec_meta = doc.metadata.get('specialty', 'N/A')
            content_preview = doc.page_content[:150].replace('\n', ' ')
            print(f"     ({i+1}) [{source} | {spec_meta}] {content_preview}...")
    
    return vectorstore


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest dữ liệu y tế vào ChromaDB")
    parser.add_argument("--file", help="Đường dẫn đến một file duy nhất để nạp (VD: data/raw/Tim_Mach/suy_tim.pdf)")
    
    args = parser.parse_args()
    
    ingest_documents(target_file=args.file)
