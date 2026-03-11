# 🏥 Medical RAG Assistant

> **Trợ Lý AI Tra Cứu Phác Đồ Điều Trị Y Tế** — Ứng dụng AI chuyên biệt hỗ trợ bác sĩ tra cứu phác đồ điều trị và chẩn đoán phân biệt, được xây dựng trên nền tảng phác đồ Bộ Y tế Việt Nam 2022–2024.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-red.svg)](https://streamlit.io)
[![LLM](https://img.shields.io/badge/LLM-Gemini_2.5_Flash-green.svg)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Tính năng

| # | Tính năng | Mô tả |
|---|-----------|-------|
| 1 | 🔍 **Phân tích ca bệnh** | Trích xuất triệu chứng, yếu tố nguy cơ, tiền sử bệnh tự động |
| 2 | 📚 **Tra cứu phác đồ RAG** | Tìm kiếm Hybrid (Vector + BM25) trên ChromaDB, trích dẫn nguồn rõ ràng |
| 3 | 🧠 **Chẩn đoán phân biệt** | Xếp hạng chẩn đoán CAO / TRUNG BÌNH / THẤP với bằng chứng ủng hộ/phản đối |
| 4 | 💊 **Cảnh báo tương tác thuốc** | Kiểm tra tự động Drug–Drug & Drug–Condition interactions |
| 5 | 🎙️ **Nhập liệu giọng nói** | Đọc triệu chứng bằng giọng nói, Gemini chuyển đổi thành văn bản y khoa |
| 6 | 🌐 **Đa ngôn ngữ (i18n)** | Giao diện + câu trả lời AI hỗ trợ song ngữ Việt–Anh |
| 7 | 📄 **Xuất báo cáo** | Tải báo cáo dạng Markdown & PDF chuyên nghiệp |
| 8 | 📊 **Dashboard thống kê** | Biểu đồ phân bố chuyên khoa, lịch sử phân tích, xuất CSV |
| 9 | 🛡️ **Safety Guardrail** | Chặn tự động các truy vấn nguy hại (tự gây hại, ma túy, chất độc) |
| 10| 📁 **Phân tích tài liệu** | Upload PDF/DOCX riêng và hỏi đáp trực tiếp với nội dung |

## 🩺 Chuyên khoa hỗ trợ

| Chuyên khoa | Nguồn phác đồ | Số chunks |
|---|---|---|
| Tim mạch | Phác đồ Viện Tim Học 2024, QĐ 2248/QĐ-BYT | ~150 |
| Hô hấp | QĐ 2767/QĐ-BYT (COPD), QĐ 63/QĐ-HHHVN (Viêm phổi) | ~140 |
| Nội tiết – Chuyển hóa | QĐ 3879/QĐ-BYT 2024 | ~134 |

## 📂 Cấu trúc dự án

```
Medical_RAG_Assistant/
├── app.py                      # Giao diện Streamlit chính (680+ dòng)
├── requirements.txt            # Danh sách thư viện Python
├── .env                        # API Key (không push lên Git)
├── .gitignore
├── .streamlit/
│   └── config.toml             # Cấu hình giao diện Streamlit
│
├── src/                        # Core modules
│   ├── diagnosis_chain.py      # Chuỗi chẩn đoán 4+1 bước
│   ├── llm_agent.py            # Gemini API wrapper + STT
│   ├── rag_engine.py           # RAG retrieval (Hybrid search)
│   ├── guardrails.py           # Safety guardrail engine
│   ├── i18n.py                 # Từ điển đa ngôn ngữ (VI/EN)
│   ├── pdf_exporter.py         # Xuất PDF (ReportLab)
│   └── report_generator.py     # Định dạng báo cáo Markdown
│
├── scripts/                    # Công cụ hỗ trợ
│   ├── ingest.py               # Nạp phác đồ vào ChromaDB
│   └── parse_docs.py           # Trích xuất text từ PDF/DOCX
│
├── data/
│   └── raw/                    # Phác đồ gốc (PDF/DOCX)
│       ├── tim_mach/
│       ├── ho_hap/
│       └── noi_tiet/
│
└── knowledge_base/
    └── chroma_db/              # Vector store (ChromaDB)
```

## 🚀 Bắt đầu nhanh

### Yêu cầu hệ thống
- Python 3.10+
- Google API Key ([Lấy tại đây](https://aistudio.google.com/apikey))
- Windows / macOS / Linux

### 1. Clone & Cài đặt

```bash
git clone https://github.com/YOUR_USERNAME/Medical_RAG_Assistant.git
cd Medical_RAG_Assistant

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Cấu hình API Key

Tạo file `.env` tại thư mục gốc:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Nạp dữ liệu phác đồ

Đặt file PDF/DOCX phác đồ vào các thư mục tương ứng:

```
data/raw/tim_mach/     ← Phác đồ Tim mạch (PDF/DOCX)
data/raw/ho_hap/       ← Phác đồ Hô hấp
data/raw/noi_tiet/     ← Phác đồ Nội tiết - Chuyển hóa
```

Chạy lệnh nạp dữ liệu vào vector store:

```bash
python scripts/ingest.py
```

### 4. Khởi chạy ứng dụng

```bash
streamlit run app.py
```

Mở trình duyệt tại `http://localhost:8501` để sử dụng.

## 🛠️ Công nghệ sử dụng

| Thành phần | Công nghệ | Phiên bản |
|---|---|---|
| **LLM** | Google Gemini 2.5 Flash | via `google-genai` SDK |
| **RAG Framework** | LangChain | >= 0.3.0 |
| **Vector Store** | ChromaDB | >= 0.5.0 |
| **Tìm kiếm** | Hybrid (Dense Vector + BM25) | — |
| **Giao diện** | Streamlit | >= 1.38.0 |
| **Xuất PDF** | ReportLab | >= 4.0 |
| **Ghi âm** | streamlit-mic-recorder | latest |
| **Triển khai** | Streamlit Community Cloud | — |

## 🔒 An toàn & Bảo mật

- **Safety Guardrail**: Tự động phát hiện và chặn truy vấn nguy hại (tự gây hại, chất độc, ma túy, bạo lực)
- **API Key**: Lưu trong `.env`, không bao giờ push lên Git
- **Data Privacy**: Toàn bộ dữ liệu xử lý local, chỉ gọi API Gemini khi cần sinh câu trả lời

## ⚕️ Tuyên bố miễn trách nhiệm

> **⚠️ Lưu ý quan trọng:** Công cụ này chỉ mang tính chất **hỗ trợ tham khảo lâm sàng**, được tạo bởi AI dựa trên phác đồ Bộ Y tế Việt Nam. **KHÔNG thay thế** phán đoán lâm sàng của bác sĩ điều trị. Mọi quyết định chẩn đoán và điều trị cần được bác sĩ có chuyên môn xem xét và phê duyệt.

---

**Được phát triển bởi Team Workshop T3** | Sử dụng phác đồ Bộ Y tế Việt Nam 2022–2024
