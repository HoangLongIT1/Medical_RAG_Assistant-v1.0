"""
report_generator.py – Định dạng báo cáo Chẩn Đoán Phân Biệt
Tạo báo cáo Markdown có cấu trúc cho hiển thị và xuất file
"""

from datetime import datetime


def format_final_report(
    case_input: str,
    specialty: str,
    case_analysis: str,
    ddx_result: str,
    summary: str,
    sources: list[dict],
    warning: str = ""
) -> str:
    """
    Tạo báo cáo Markdown hoàn chỉnh.
    
    Returns:
        str: Báo cáo Markdown
    """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    specialty_display = specialty if specialty else "Đa khoa"
    
    report_parts = []
    
    # Header
    report_parts.append(f"""# 📋 Báo Cáo Chẩn Đoán Phân Biệt
**Thời gian:** {timestamp}  
**Chuyên khoa:** {specialty_display}  
**Mô hình AI:** Gemini 2.5 Flash

---""")
    
    # Cảnh báo an toàn (nếu có)
    if warning:
        report_parts.append(f"\n{warning}\n")
    
    # Ca bệnh gốc
    report_parts.append(f"""
## 🏥 Ca Bệnh

{case_input}

---""")
    
    # Bước 1: Phân tích
    report_parts.append(f"""
## 🔍 Phân Tích Ca Bệnh

{case_analysis}

---""")
    
    # Bước 2: Nguồn tham khảo
    if sources:
        sources_text = "\n".join([
            f"- **{s.get('source', 'N/A')}** ({s.get('specialty', '')})"
            for s in sources
        ])
        report_parts.append(f"""
## 📚 Nguồn Phác Đồ Tham Khảo

{sources_text}

---""")
    
    # Bước 3: CĐPB
    report_parts.append(f"""
## 🧠 Chẩn Đoán Phân Biệt

{ddx_result}

---""")
    
    # Bước 4: Tóm tắt
    report_parts.append(f"""
## 📝 Tóm Tắt & Khuyến Nghị

{summary}

---""")
    
    # Disclaimer
    report_parts.append("""
## ⚕️ Tuyên Bố Miễn Trách

> **Lưu ý quan trọng:** Kết quả này chỉ mang tính chất **hỗ trợ tham khảo lâm sàng**, 
> được tạo bởi AI dựa trên phác đồ Bộ Y tế Việt Nam. 
> **KHÔNG thay thế** phán đoán lâm sàng của bác sĩ điều trị.
> Mọi quyết định chẩn đoán và điều trị cần được bác sĩ có chuyên môn xem xét và phê duyệt.
""")
    
    return "\n".join(report_parts)


def export_report_markdown(report: str, filename: str = None) -> str:
    """
    Xuất báo cáo ra file Markdown.
    
    Returns:
        str: Nội dung report (để download từ Streamlit)
    """
    return report
