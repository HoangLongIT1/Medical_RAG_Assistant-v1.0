"""
i18n.py – Từ điển Đa ngôn ngữ (Tiếng Việt / English)
Chứa tất cả các chuỗi giao diện và nhãn dùng trong app.py
"""

LANG = {
    "vi": {
        # ── App Header & Tabs ──
        "app_title": "🏥 Trợ Lý AI Y Tế Toàn Diện",
        "app_subtitle": "Hỗ trợ chẩn đoán phân biệt & Phân tích tài liệu phác đồ",
        "tab_rag": "🔍 Hỗ Trợ Chẩn Đoán (Kho Dữ Liệu)",
        "tab_doc": "📑 Phân Tích Phác Đồ (File Tải Lên)",
        "tab_dash": "📊 Dashboard Thống Kê",

        # ── Tab 1: Form nhập liệu ──
        "demo_cases": "📋 Chọn nhanh ca bệnh mẫu:",
        "clinical_info": "📝 Thông tin lâm sàng",
        "symptoms_label": "Bệnh sử & Triệu chứng:",
        "symptoms_placeholder": "Ví dụ: Bệnh nhân nam, 58 tuổi, vào viện vì đau ngực trái...",
        "specialty_label": "🏥 Chuyên khoa dự định:",
        "age_label": "🎂 Tuổi bệnh nhân:",
        "sex_label": "🚻 Giới tính:",
        "sex_options": ["Chưa chọn", "Nam", "Nữ"],
        "btn_analyze": "Trích xuất CĐPB & Đề xuất điều trị",

        # Specialty options
        "auto_detect_specialty": "Tự động nhận diện",
        "auto_detect_specialty_short": "Tự động",
        "cardiology": "Tim mạch",
        "respiratory": "Hô hấp",
        "endocrinology": "Nội tiết - Chuyển hóa",
        "unspecified_sex": "Chưa chọn",

        # ── Tab 1: Errors ──
        "error_empty_input": "⚠️ Vui lòng nhập mô tả triệu chứng!",
        "error_api_key": "⚠️ Lỗi hệ thống: Chưa cấu hình API Key trong file .env!",
        "error_occurred": "Đã xảy ra lỗi",
        "analysis_results": "Kết Quả Phân Tích",

        # ── Tab 1: Processing steps ──
        "step_analysis": "⏳ Đang phân tích ca bệnh...",
        "step_search": "⏳ Đang tra cứu phác đồ y tế...",
        "step_ddx": "Đang xử lý",
        "step1_title": "🔍 Bước 1: Phân tích ca bệnh",
        "step2_title": "📚 Bước 2: Nguồn phác đồ tham khảo",
        "no_sources_found": "Không tìm thấy tài liệu liên quan.",
        "ddx_title": "Chẩn Đoán Phân Biệt",
        "summary_title": "Tóm Tắt & Khuyến Nghị",
        "result_success": "✅ Hoàn thành phân tích!",

        "disclaimer": "Kết quả chỉ mang tính tham khảo. Cần bác sĩ chuyên khoa xem xét trước khi áp dụng.",

        # ── Follow-up Chat ──
        "chat_followup_title": "💬 Thảo luận thêm về ca bệnh",
        "chat_followup_info": "Bác sĩ có thể đặt thêm câu hỏi về phác đồ, liều dùng hoặc các tình huống lâm sàng liên quan bên dưới.",
        "chat_followup_placeholder": "Hỏi thêm về ca bệnh này (VD: Giải thích kỹ phần xử trí...)",

        # ── Tab 2: Document Q&A ──
        "doc_upload_title": "📄 Tải lên Tài liệu Phác đồ Cá nhân hóa",
        "doc_upload_info": "Hệ thống hỗ trợ đọc và tương tác trực tiếp nội dung các phác đồ định dạng PDF/DOCX. Có thể tải lên nhiều file cùng lúc (Tối đa 20 file, mỗi file ≤ 100MB).",
        "doc_multi_loaded": "Đã tải và đọc xong",
        "doc_files_count": "file",
        "doc_total_chars": "tổng ký tự",
        "doc_upload_label": "Tải lên tài liệu y khoa:",
        "doc_reading": "Đang đọc nội dung tài liệu...",
        "doc_upload_success": "Đã tải và đọc xong tài liệu",
        "characters": "ký tự",
        "doc_chat_title": "Hội thoại với tài liệu",
        "doc_chat_placeholder": "Hỏi gì đó về phác đồ này...",

        # ── Tab 3: Dashboard ──
        "dash_title": "Bảng Điều Khiển & Thống Kê",
        "dash_desc": "Cái nhìn tổng quan về hệ thống và dữ liệu chuyên khoa đã phân tích.",
        "dash_total": "Tổng ca đã phân tích",
        "dash_data": "Số Chunk dữ liệu y tế (VectorDB)",
        "dash_speed": "Tốc độ truy xuất (avg)",
        "chart_title": "📈 Phân bố chuyên khoa",
        "table_title": "📋 Lịch sử chi tiết (Gần đây)",
        "btn_export_csv": "⬇️ Xuất file CSV (Tất cả ca bệnh)",
        "sidebar_info": "Thông tin hệ thống",
        "sidebar_history": "Lịch sử phiên",
        "history_symptoms": "Triệu chứng",
        "history_time": "Thời gian",
        "no_recent_cases": "Chưa có ca bệnh nào được phân tích.",
        "insufficient_data": "Chưa đủ dữ liệu để vẽ biểu đồ.",
        "no_cases_yet": "Chưa có ca bệnh nào.",
        "drug_warning_title": "⚠️ Cảnh báo Tương tác & An toàn Thuốc",
        "no_drug_warning": "Không phát hiện tương tác thuốc nghiêm trọng trong dữ liệu cung cấp.",
        "voice_rec_label": "Ghi âm triệu chứng",
        "voice_processing": "Đang chuyển đổi giọng nói...",
        "step_drug_check": "⏳ Đang kiểm tra tương tác thuốc...",

        # ── Footer ──
        "footer_text": "Công cụ hỗ trợ lâm sàng — Dựa trên phác đồ Bộ Y tế Việt Nam. Không thay thế phán đoán y khoa.",

        # ── Prompt instruction ──
        "prompt_instruction": "Bạn PHẢI trả lời bằng TIẾNG VIỆT, sử dụng văn phong y khoa chuyên nghiệp và chuẩn mực của Việt Nam."
    },

    "en": {
        # ── App Header & Tabs ──
        "app_title": "🏥 Comprehensive Medical AI Assistant",
        "app_subtitle": "Differential Diagnosis Support & Protocol Document Analysis",
        "tab_rag": "🔍 Diagnosis Support (Knowledge Base)",
        "tab_doc": "📑 Protocol Analysis (File Upload)",
        "tab_dash": "📊 Statistical Dashboard",

        # ── Tab 1: Form ──
        "demo_cases": "📋 Quick load sample cases:",
        "clinical_info": "📝 Clinical Information",
        "symptoms_label": "Medical History & Symptoms:",
        "symptoms_placeholder": "E.g., 58-year-old male presenting with left chest pain...",
        "specialty_label": "🏥 Target Specialty:",
        "age_label": "🎂 Patient Age:",
        "sex_label": "🚻 Gender:",
        "sex_options": ["Unspecified", "Male", "Female"],
        "btn_analyze": "Extract DDx & Propose Treatment",

        # Specialty options
        "auto_detect_specialty": "Auto-detect",
        "auto_detect_specialty_short": "Auto",
        "cardiology": "Cardiology",
        "respiratory": "Respiratory",
        "endocrinology": "Endocrinology",
        "unspecified_sex": "Unspecified",

        # ── Tab 1: Errors ──
        "error_empty_input": "⚠️ Please enter symptom descriptions!",
        "error_api_key": "⚠️ System Error: No API Key configured in .env file!",
        "error_occurred": "An error occurred",
        "analysis_results": "Analysis Results",

        # ── Tab 1: Processing steps ──
        "step_analysis": "⏳ Analyzing clinical case...",
        "step_search": "⏳ Retrieving medical protocols...",
        "step_ddx": "Processing",
        "step1_title": "🔍 Step 1: Case Analysis",
        "step2_title": "📚 Step 2: Protocol References",
        "no_sources_found": "No relevant documents found.",
        "ddx_title": "Differential Diagnosis",
        "summary_title": "Summary & Recommendations",
        "result_success": "✅ Analysis complete!",

        # ── Tab 1: Report download ──
        "btn_dl_md": "📥 Download Report (Markdown)",
        "btn_dl_docx": "📥 Download Report (DOCX)",
        "report_title": "Differential Diagnosis Report",
        "report_title_short": "DDx Report",
        "report_specialty": "Specialty",
        "report_case_info": "Case Info",
        "report_ddx": "Differential Diagnosis",
        "report_summary": "Summary & Recommendations",
        "disclaimer": "This tool is for reference only and does not replace the clinical judgment of a physician.",

        # ── Follow-up Chat ──
        "chat_followup_title": "💬 Case Follow-up Discussion",
        "chat_followup_info": "You can ask additional questions about guidelines, dosage, or clinical scenarios below.",
        "chat_followup_placeholder": "Ask something more about this case (E.g.: Explain the treatment part...)",

        # ── Tab 2: Document Q&A ──
        "doc_upload_title": "📄 Upload Personalized Protocol Documents",
        "doc_upload_info": "Supports reading and interacting with PDF/DOCX protocol documents. You can upload multiple files at once (Max 20 files, each ≤ 100MB).",
        "doc_multi_loaded": "Loaded and processed",
        "doc_files_count": "file(s)",
        "doc_total_chars": "total characters",
        "doc_upload_label": "Upload medical document:",
        "doc_reading": "Reading document content...",
        "doc_upload_success": "Document loaded and processed",
        "characters": "characters",
        "doc_chat_title": "Chat with Document",
        "doc_chat_placeholder": "Ask something about this protocol...",

        # ── Tab 3: Dashboard ──
        "dash_title": "Dashboard & Statistics",
        "dash_desc": "An overview of the system and analyzed specialty data.",
        "dash_total": "Total Analyzed Cases",
        "dash_data": "Medical Data Chunks (VectorDB)",
        "dash_speed": "Retrieval Speed (avg)",
        "chart_title": "📈 Specialty Distribution",
        "table_title": "📋 Detailed History (Recent)",
        "btn_export_csv": "⬇️ Export CSV File (All cases)",
        "sidebar_info": "System Information",
        "sidebar_history": "Session History",
        "history_symptoms": "Symptoms",
        "history_time": "Time",
        "no_recent_cases": "No cases have been analyzed yet.",
        "insufficient_data": "Insufficient data to display the chart.",
        "no_cases_yet": "No cases available.",
        "drug_warning_title": "⚠️ Drug Interaction & Safety Warning",
        "no_drug_warning": "No serious drug interactions detected in the provided data.",
        "voice_rec_label": "Record Symptoms",
        "voice_processing": "Processing voice...",
        "step_drug_check": "⏳ Checking drug interactions...",

        # ── Footer ──
        "footer_text": "Clinical support tool — Based on Vietnam MOH Protocols. Does not replace medical judgment.",

        # ── Prompt instruction ──
        "prompt_instruction": "You MUST respond in ENGLISH, using professional and standard medical terminology."
    }
}
