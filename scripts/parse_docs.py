"""
parse_docs.py – Parser tài liệu y tế tiếng Việt
Sử dụng PyMuPDF (fitz) cho PDF và docx2txt cho DOCX
Chunking theo token với overlap
"""

import os
import re
import fitz  # PyMuPDF
import docx2txt


def extract_text_from_pdf(pdf_path: str) -> str:
    """Trích xuất text từ file PDF bằng PyMuPDF (hỗ trợ tốt tiếng Việt)."""
    doc = fitz.open(pdf_path)
    text_parts = []
    for page_num, page in enumerate(doc, 1):
        page_text = page.get_text("text")
        if page_text.strip():
            text_parts.append(f"\n--- Trang {page_num} ---\n{page_text}")
    doc.close()
    return "\n".join(text_parts)


def extract_text_from_docx(docx_path: str) -> str:
    """Trích xuất text từ file DOCX."""
    return docx2txt.process(docx_path)


def clean_text(text: str) -> str:
    """Làm sạch văn bản y tế tiếng Việt."""
    # Xóa ký tự đặc biệt thừa nhưng giữ dấu tiếng Việt
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'[^\S\n]+', ' ', text)
    # Giữ lại các ký tự y tế quan trọng
    text = text.strip()
    return text


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[dict]:
    """
    Chia văn bản thành các chunks theo ký tự với overlap.
    
    Args:
        text: Văn bản đầu vào
        chunk_size: Kích thước mỗi chunk (ký tự)
        overlap: Số ký tự trùng lặp giữa 2 chunks liên tiếp
    
    Returns:
        List[dict] với keys: 'content', 'chunk_index'
    """
    chunks = []
    start = 0
    chunk_index = 0
    
    while start < len(text):
        end = start + chunk_size
        
        # Cố gắng cắt tại cuối câu gần nhất
        if end < len(text):
            # Tìm dấu chấm câu gần nhất trước vị trí end
            last_period = text.rfind('.', start + chunk_size // 2, end + 100)
            last_newline = text.rfind('\n', start + chunk_size // 2, end + 100)
            cut_point = max(last_period, last_newline)
            if cut_point > start:
                end = cut_point + 1
        
        chunk_content = text[start:end].strip()
        if chunk_content:
            chunks.append({
                'content': chunk_content,
                'chunk_index': chunk_index
            })
            chunk_index += 1
        
        start = end - overlap
        if start >= len(text):
            break
    
    return chunks


def detect_specialty(file_path: str) -> str:
    """Nhận diện chuyên khoa từ đường dẫn thư mục."""
    path_lower = file_path.lower().replace("\\", "/")
    if "tim_mach" in path_lower:
        return "Tim mạch"
    elif "ho_hap" in path_lower:
        return "Hô hấp"
    elif "noi_tiet" in path_lower:
        return "Nội tiết - Chuyển hóa"
    return "Chung"


def parse_document(file_path: str) -> list[dict]:
    """
    Parse một tài liệu y tế và trả về danh sách chunks có metadata.
    
    Returns:
        List[dict] với keys: 'content', 'metadata'
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        raw_text = extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        raw_text = extract_text_from_docx(file_path)
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    else:
        print(f"⚠️ Bỏ qua file không hỗ trợ: {file_path}")
        return []
    
    cleaned = clean_text(raw_text)
    if not cleaned:
        print(f"⚠️ File rỗng sau khi làm sạch: {file_path}")
        return []
    
    chunks = chunk_text(cleaned)
    specialty = detect_specialty(file_path)
    filename = os.path.basename(file_path)
    
    results = []
    for chunk in chunks:
        results.append({
            'content': chunk['content'],
            'metadata': {
                'source': filename,
                'file_path': file_path,
                'specialty': specialty,
                'chunk_index': chunk['chunk_index'],
                'total_chunks': len(chunks)
            }
        })
    
    print(f"✅ Đã parse {filename}: {len(chunks)} chunks | Chuyên khoa: {specialty}")
    return results


def parse_all_documents(data_dir: str) -> list[dict]:
    """
    Parse tất cả tài liệu trong thư mục data/raw.
    
    Args:
        data_dir: Đường dẫn tới thư mục data/raw
    
    Returns:
        Tổng hợp tất cả chunks từ tất cả files
    """
    all_chunks = []
    supported_exts = {'.pdf', '.docx', '.doc', '.txt'}
    
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in supported_exts:
                file_path = os.path.join(root, file)
                chunks = parse_document(file_path)
                all_chunks.extend(chunks)
    
    print(f"\n📊 Tổng cộng: {len(all_chunks)} chunks từ thư mục {data_dir}")
    return all_chunks


if __name__ == "__main__":
    import sys
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data/raw"
    results = parse_all_documents(data_dir)
    print(f"Kết quả: {len(results)} chunks")
