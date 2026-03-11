# 📋 Lịch sử thay đổi (Changelog)

Tất cả các thay đổi đáng kể của dự án được ghi nhận trong file này.

---

## [1.0.0] — 2026-03-11

### ✅ Phát hành chính thức — Đầy đủ tính năng

#### Core Engine
- **RAG Pipeline**: LangChain + ChromaDB + BM25 Hybrid Search
- **LLM**: Gemini 2.5 Flash (via `google-genai` SDK)
- **Diagnosis Chain**: Chuỗi chẩn đoán 4+1 bước (Phân tích → RAG → CĐPB → Cảnh báo thuốc → Tóm tắt)
- **Safety Guardrail**: Phát hiện và chặn truy vấn nguy hại

#### Giao diện
- **Tab 1 — Chẩn đoán phân biệt**: Nhập ca bệnh, chọn chuyên khoa, nhận kết quả streaming
- **Tab 2 — Phân tích tài liệu**: Upload PDF/DOCX, hỏi đáp trực tiếp với nội dung
- **Tab 3 — Dashboard**: Thống kê, biểu đồ phân bố chuyên khoa, xuất CSV
- **7 ca bệnh mẫu**: Bao gồm 3 ca đơn khoa + 4 ca giao thoa đa chuyên khoa

#### Tính năng nâng cao
- **Đa ngôn ngữ (i18n)**: Hỗ trợ song ngữ Việt–Anh cho toàn bộ UI và câu trả lời AI
- **Xuất PDF**: Báo cáo chuyên nghiệp sử dụng ReportLab
- **Cảnh báo tương tác thuốc**: Kiểm tra Drug–Drug & Drug–Condition tự động
- **Nhập giọng nói**: Ghi âm triệu chứng bằng microphone, Gemini STT chuyển đổi

#### Dữ liệu
- 3 phác đồ Bộ Y tế Việt Nam (Tim mạch, Hô hấp, Nội tiết)
- 424 chunks trong ChromaDB vector store
- Hỗ trợ tìm kiếm Hybrid (Dense Vector + BM25)

---

## [0.1.0] — 2026-03-04

### 🏗️ MVP — Phiên bản khởi tạo

- Setup project structure
- Implement basic RAG pipeline
- Create Streamlit UI
- Add Safety Guardrail
- Ingest 3 medical protocols into ChromaDB
