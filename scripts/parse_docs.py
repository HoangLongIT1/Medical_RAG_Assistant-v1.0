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
    """Trích xuất text từ file PDF bằng PyMuPDF với xử lý ghép dòng thông minh."""
    doc = fitz.open(pdf_path)
    text_parts = []
    for page_num, page in enumerate(doc, 1):
        # Sử dụng 'dict' để lấy khối văn bản, giúp giữ thứ tự đọc tốt hơn
        blocks = page.get_text("blocks")
        page_text = ""
        for b in blocks:
            # b[4] chứa nội dung text của khối
            block_content = b[4].strip()
            if block_content:
                # Thay thế các dấu xuống dòng đơn lẻ trong khối bằng khoảng trắng 
                # để tránh việc bị ngắt dòng vô lý giữa từ
                block_content = block_content.replace("\n", " ")
                page_text += block_content + "\n"
        
        if page_text.strip():
            text_parts.append(f"\n--- Trang {page_num} ---\n{page_text}")
    doc.close()
    return "\n".join(text_parts)


def extract_text_from_docx(docx_path: str) -> str:
    """Trích xuất text từ file DOCX."""
    return docx2txt.process(docx_path)


def clean_text(text: str) -> str:
    """Làm sạch văn bản y tế tiếng Việt, xử lý các lỗi font, xuống dòng sai, và lọc rác (Mục lục, Tài liệu tham khảo)."""
    
    # 0. Truncate at "Tài liệu tham khảo" (thường ở phần cuối)
    # Loại bỏ phụ lục / tài liệu tham khảo nếu nó nằm ở nửa cuối văn bản
    ref_match = re.search(r'\n\s*TÀI LIỆU THAM KHẢO\s*\n', text, re.IGNORECASE)
    if ref_match and ref_match.start() > len(text) * 0.5:
        text = text[:ref_match.start()]
    
    # 1. Xử lý dấu gạch nối ngắt từ (Ví dụ: "chẩn- \n đoán" -> "chẩn đoán")
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    
    # 2. Loại bỏ các dòng Mục lục (chứa nhiều dấu chấm liên tiếp e.g "..........")
    text = re.sub(r'^.*\.{5,}.*$', '', text, flags=re.MULTILINE)
    
    # 3. Lọc bỏ các dòng chỉ chứa số (thường là số trang bị tách rời)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^Trang\s+\d+(\/\d+)?$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    
    # 4. Xử lý lỗi font, giữ lại ký tự in được và newline
    text = "".join(ch for ch in text if ch.isprintable() or ch == '\n')

    # 5. Phục hồi các câu bị rớt dòng (nếu dòng kết thúc bằng chữ thường hoặc dấu phẩy thì nối nó với dòng tiếp theo)
    # Tạm thay \n thành khoảng trắng nếu câu chưa kết thúc bằng dấu câu chính (., :, ?, !)
    lines = text.split('\n')
    cleaned_lines = []
    current_sentence = ""
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            if current_sentence:
                cleaned_lines.append(current_sentence)
                current_sentence = ""
            continue
            
        if current_sentence:
            # Nếu câu đang chờ kết nối
            if current_sentence[-1] in ['.', ':', '?', '!', ';']:
                cleaned_lines.append(current_sentence)
                current_sentence = line_stripped
            else:
                current_sentence += " " + line_stripped
        else:
            current_sentence = line_stripped
            
    if current_sentence:
        cleaned_lines.append(current_sentence)
        
    text = "\n\n".join(cleaned_lines)

    # 6. Chuẩn hóa khoảng trắng
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


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
        # Loại bỏ các đoạn văn quá ngắn (dưới 50 ký tự) vì không mang lại giá trị lâm sàng và làm nhiễu vector db
        if chunk_content and len(chunk_content) >= 50:
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
