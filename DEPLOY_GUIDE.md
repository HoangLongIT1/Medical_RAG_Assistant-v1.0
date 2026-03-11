# 🚀 Hướng Dẫn Triển Khai (Deploy Guide)

Tài liệu hướng dẫn đưa **Medical RAG Assistant** lên môi trường production.

---

## Phương án 1: Chạy Local (Development)

### Yêu cầu
- Python 3.10+
- Google API Key cho Gemini 2.5 Flash

### Các bước

```bash
# 1. Tạo môi trường ảo
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 2. Cài đặt thư viện
pip install -r requirements.txt

# 3. Cấu hình API Key
# Tạo file .env với nội dung:
# GOOGLE_API_KEY=your_api_key_here

# 4. Nạp dữ liệu phác đồ (chỉ cần chạy 1 lần)
python scripts/ingest.py

# 5. Khởi chạy
streamlit run app.py
```

---

## Phương án 2: Streamlit Community Cloud (Production)

### Bước 1 — Push code lên GitHub

```bash
git init
git add .
git commit -m "Medical RAG Assistant v1.0"
git branch -M main
git remote add origin https://github.com/USERNAME/Medical_RAG_Assistant.git
git push -u origin main
```

> **Lưu ý:** File `.gitignore` đã loại bỏ `.env`, `venv/`, `__pycache__/` để bảo vệ API Key và giảm kích thước repo.

### Bước 2 — Kết nối Streamlit Cloud

1. Truy cập [share.streamlit.io](https://share.streamlit.io/) → đăng nhập bằng GitHub.
2. Nhấn **"New app"** và điền:
   | Trường | Giá trị |
   |---|---|
   | Repository | `USERNAME/Medical_RAG_Assistant` |
   | Branch | `main` |
   | Main file path | `app.py` |

3. **⚠️ QUAN TRỌNG:** Mở **Advanced settings** → tab **Secrets** → dán nội dung:
   ```toml
   GOOGLE_API_KEY = "your_real_gemini_api_key"
   ```

### Bước 3 — Deploy

Nhấn **"Deploy!"**. Streamlit sẽ:
1. Cài đặt thư viện từ `requirements.txt` (~1–3 phút)
2. Khởi chạy ứng dụng
3. Hiển thị URL công khai (dạng `https://your-app.streamlit.app`)

---

## ⚠️ Lưu ý quan trọng

| Mục | Chi tiết |
|---|---|
| **Vector Store** | Thư mục `knowledge_base/chroma_db/` được push lên GitHub, do đó ứng dụng có thể chạy ngay mà không cần nạp dữ liệu lại. |
| **API Quota** | Hiệu suất phụ thuộc vào gói dịch vụ Gemini API Key. Free Tier có giới hạn 15 RPM / 1M TPM. Tránh vượt quá quota để app không bị lỗi giữa chừng. |
| **Kích thước repo** | Do chứa vector store (~50MB), lần clone đầu có thể mất thời gian. |
| **Bảo mật** | **KHÔNG BAO GIỜ** commit file `.env` hoặc hard-code API Key. Luôn dùng Secrets của Streamlit Cloud. |

---

## 🔄 Cập nhật phác đồ mới

Khi có phác đồ mới, chỉ cần:

```bash
# 1. Đặt file PDF/DOCX vào thư mục tương ứng
#    data/raw/tim_mach/  hoặc  ho_hap/  hoặc  noi_tiet/

# 2. Chạy lại script nạp dữ liệu
python scripts/ingest.py

# 3. Commit và push
git add knowledge_base/
git commit -m "Update medical protocols"
git push
```

Streamlit Cloud sẽ tự động redeploy khi phát hiện commit mới trên `main`.
