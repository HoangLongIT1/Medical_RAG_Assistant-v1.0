# 🏗️ Kiến trúc hệ thống (Architecture)

Tài liệu mô tả kiến trúc kỹ thuật của **Medical RAG Assistant**.

---

## Tổng quan

```
┌──────────────────────────────────────────────────────────────┐
│                     STREAMLIT UI (app.py)                    │
│  ┌──────────┐  ┌────────────────┐  ┌───────────────────┐    │
│  │  Tab 1    │  │    Tab 2       │  │     Tab 3         │    │
│  │ Chẩn đoán │  │   Double RAG   │  │   Dashboard       │    │
│  │ phân biệt │  │ (Doc + System) │  │   & Thống kê      │    │
│  │  (RAG)    │  │                │  │                   │    │
│  └─────┬─────┘  └───────┬────────┘  └───────────────────┘    │
│        │                │                                     │
│  ┌─────▼─────┐   ┌──────▼───────┐   ┌───────────────────┐   │
│  │ 🎙️ Voice  │   │ 📄 Double RAG│   │ 🌐 i18n (VI/EN)  │   │
│  │   Input   │   │ Comparative  │   │   src/i18n.py     │   │
│  │ (Whisper) │   │ Analysis     │   │                       │    │
│  └─────┬─────┘   └──────────────┘   └───────────────────┘   │
└────────┼─────────────────────────────────────────────────────┘
         │
┌────────▼─────────────────────────────────────────────────────┐
│                   DIAGNOSIS CHAIN (4+1 bước)                 │
│              src/diagnosis_chain.py                           │
│                                                               │
│  1️⃣ Phân tích ca bệnh (CASE_ANALYSIS_PROMPT)                │
│                   ↓                                           │
│  2️⃣ RAG Retrieval (Hybrid: Vector + BM25)                   │
│                   ↓                                           │
│  3️⃣ Chẩn đoán phân biệt (DIFFERENTIAL_DIAGNOSIS_PROMPT)     │
│                   ↓                                           │
│  3.5️⃣ Kiểm tra tương tác thuốc (DRUG_INTERACTION_PROMPT)     │
│                   ↓                                           │
│  4️⃣ Tóm tắt & Khuyến nghị (REPORT_SUMMARY_PROMPT)          │
└──────────────────────────────────────────────────────────────┘
         │                          │
┌────────▼───────────┐     ┌────────▼───────────┐
│   LLM AGENT        │     │   RAG ENGINE       │ 
│ src/llm_agent.py   │     │ src/rag_engine.py  │
│                    │     │                    │
│ • Gemini 2.5 Flash │     │ • ChromaDB (Vector)│
│ • Double-RAG Logic │     │ • BM25 Reranking   │
│ • Prompts Manager  │     │ • Hybrid Search    │
│ • Audio Transcribe │     │ • > 4000 chunks    │
└────────────────────┘     └────────────────────┘
         │
┌────────▼───────────┐     ┌──────────────────────┐
│  SAFETY GUARDRAIL  │     │   PDF EXPORTER       │ 
│ src/guardrails.py  │     │ src/pdf_exporter.py  │
│                    │     │                      │
│ • Hard block:      │     │ • ReportLab Platypus │
│   - Self-harm      │     │ • Unicode VN support │
│   - Poison/Drugs   │     │ • Markdown → PDF     │
│   - Violence       │     │ • Multi-page layout  │
└────────────────────┘     └──────────────────────┘

---

## Tính năng nổi bật

### Double RAG (Tab 2)
Cơ chế truy vấn song song giữa **Dữ liệu người dùng tải lên** và **Kho tri thức phác đồ hệ thống**. AI sẽ thực hiện so sánh, đối chiếu và chỉ ra các điểm khác biệt hoặc bổ sung giữa tài liệu lâm sàng cá nhân và hướng dẫn chuẩn của Bộ Y tế.

### Incremental Ingest & Anti-Noise Parser
- **Smart Ingest:** Tự động nhận diện file đã nạp, chỉ nạp thêm file mới để tiết kiệm Quota API.
- **Anti-Noise:** 
    - Loại bỏ mục lục (Table of Contents) dựa trên pattern dấu chấm `...`.
    - Tự động ngắt bỏ phần "Tài liệu tham khảo" ở cuối file.
    - Ghép nối các câu bị rớt dòng (Broken lines) để giữ tính toàn vẹn của y lệnh.

---

## Luồng xử lý chính

### Chẩn đoán phân biệt (Tab 1)

```
Người dùng nhập ca bệnh (Text/Voice)
         │
         ▼
   Safety Guardrail ─── Nguy hại? ──→ CHẶN (hiện cảnh báo)
         │
         ▼ (An toàn)
   Bước 1: Phân tích ca bệnh (LLM)
   → Trích xuất triệu chứng, yếu tố nguy cơ, tiền sử
         │
         ▼
   Bước 2: RAG Retrieval (ChromaDB + BM25)
   → Tìm kiếm Hybrid k=5
   → Lấy phác đồ liên quan nhất từ > 4000 chunks
         │
         ▼
   Bước 3: Chẩn đoán phân biệt (LLM)
   → Xếp hạng CAO / TRUNG BÌNH / THẤP
   → Trích dẫn nguồn phác đồ chi tiết
         │
         ▼
   Bước 3.5: Kiểm tra tương tác thuốc (LLM)
   → Cảnh báo tương tác thuốc-thuốc, thuốc-bệnh lý
         │
         ▼
   Bước 4: Tóm tắt & Khuyến nghị (LLM)
   → Ưu tiên xử trí, CLS đề xuất, theo dõi
         │
         ▼
   Hiển thị kết quả + Nút tải MD/PDF (Scroll-to-top)
```

---

## Modules

| Module | Chức năng | Trạng thái |
|---|---|---|
| `app.py` | UI Streamlit, Tab management, Double-RAG logic | ~660 dòng |
| `src/diagnosis_chain.py` | Luồng chẩn đoán 5 bước, evidence ranking | ~240 dòng |
| `src/llm_agent.py` | Gemini API, Double-RAG Prompts, Audio | ~210 dòng |
| `src/rag_engine.py` | Hybrid Search (Vector + BM25) | ~200 dòng |
| `src/guardrails.py` | An toàn y tế & cộng đồng | ~120 dòng |
| `src/i18n.py` | Đa ngôn ngữ (VI/EN), Footer & Header | ~200 dòng |
| `src/pdf_exporter.py` | Xuất báo cáo chuyên nghiệp | ~250 dòng |
| `scripts/ingest.py` | Nạp data thông minh, bảo vệ Key Free | ~150 dòng |
| `scripts/parse_docs.py` | Parser nâng cao, lọc noise mục lục | ~170 dòng |

