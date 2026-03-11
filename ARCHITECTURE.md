# 🏗️ Kiến trúc hệ thống (Architecture)

Tài liệu mô tả kiến trúc kỹ thuật của **Medical RAG Assistant**.

---

## Tổng quan

```
┌──────────────────────────────────────────────────────────────┐
│                     STREAMLIT UI (app.py)                    │
│  ┌──────────┐  ┌────────────────┐  ┌───────────────────┐    │
│  │  Tab 1    │  │    Tab 2       │  │     Tab 3         │    │
│  │ Chẩn đoán │  │ Phân tích      │  │   Dashboard       │    │
│  │ phân biệt │  │ tài liệu       │  │   & Thống kê      │    │
│  └─────┬─────┘  └───────┬────────┘  └───────────────────┘    │
│        │                │                                     │
│  ┌─────▼─────┐   ┌──────▼───────┐   ┌───────────────────┐   │
│  │ 🎙️ Voice  │   │ 📄 Doc Q&A   │   │ 🌐 i18n (VI/EN)  │   │
│  │   Input   │   │   Stream     │   │   src/i18n.py     │   │
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
│     Kiểm tra tương tác thuốc (DRUG_INTERACTION_PROMPT)       │
│                   ↓                                           │
│  4️⃣ Tóm tắt & Khuyến nghị (REPORT_SUMMARY_PROMPT)          │
└──────────────────────────────────────────────────────────────┘
         │                          │
┌────────▼───────────┐     ┌────────▼───────────┐
│   LLM AGENT        │     │   RAG ENGINE       │ 
│ src/llm_agent.py   │     │ src/rag_engine.py  │
│                    │     │                    │
│ • Gemini 2.5 Flash │     │ • ChromaDB         │
│ • generate_response│     │ • BM25 Reranking   │
│ • transcribe_audio │     │ • Hybrid Search    │
│ • 8192 max tokens  │     │ • 424 chunks       │
└────────────────────┘     └────────────────────┘
         │
┌────────▼───────────┐     ┌──────────────────────┐
│  SAFETY GUARDRAIL  │     │   PDF EXPORTER       │ 
│ src/guardrails.py  │     │ src/pdf_exporter.py  │
│                    │     │                      │
│ • Hard block:      │     │ • ReportLab (Platypus│
│   - Self-harm      │     │ • Unicode VN support │
│   - Poison/Drugs   │     │ • Markdown → HTML →  │
│   - Violence       │     │   PDF conversion     │
└────────────────────┘     └──────────────────────┘
```

---

## Luồng xử lý chính

### Chẩn đoán phân biệt (Tab 1)

```
Người dùng nhập ca bệnh
         │
         ▼
   Safety Guardrail ─── Nguy hại? ──→ CHẶN (hiện cảnh báo)
         │
         ▼ (An toàn)
   Bước 1: Phân tích ca bệnh
   → Trích xuất triệu chứng, yếu tố nguy cơ, tiền sử
         │
         ▼
   Bước 2: RAG Retrieval
   → Tìm kiếm Hybrid trên ChromaDB (k=5)
   → Lấy phác đồ liên quan nhất
         │
         ▼
   Bước 3: Chẩn đoán phân biệt
   → Xếp hạng CAO / TRUNG BÌNH / THẤP
   → Trích dẫn nguồn phác đồ
         │
         ▼
   Bước 3.5: Kiểm tra tương tác thuốc
   → Drug–Drug, Drug–Condition
         │
         ▼
   Bước 4: Tóm tắt & Khuyến nghị
   → Ưu tiên xử trí, cận lâm sàng đề xuất
         │
         ▼
   Hiển thị kết quả + Nút tải MD/PDF
```

---

## Modules

| Module | Chức năng | Size |
|---|---|---|
| `app.py` | Giao diện Streamlit chính | ~680 dòng |
| `src/diagnosis_chain.py` | Chuỗi chẩn đoán 4+1 bước | ~225 dòng |
| `src/llm_agent.py` | Gemini API wrapper + Prompts + STT | ~233 dòng |
| `src/rag_engine.py` | RAG retrieval (Vector + BM25) | ~150 dòng |
| `src/guardrails.py` | Safety guardrail engine | ~120 dòng |
| `src/i18n.py` | Từ điển đa ngôn ngữ (VI/EN, 80+ keys) | ~197 dòng |
| `src/pdf_exporter.py` | Xuất PDF (ReportLab Platypus) | ~210 dòng |
| `src/report_generator.py` | Định dạng báo cáo Markdown | ~107 dòng |
| `scripts/ingest.py` | Nạp phác đồ vào ChromaDB | ~130 dòng |
| `scripts/parse_docs.py` | Trích xuất text từ PDF/DOCX | ~140 dòng |
