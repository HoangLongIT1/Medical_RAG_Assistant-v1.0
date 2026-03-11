"""
app.py – Giao diện Streamlit chính
Trợ Lý AI Tra Cứu Phác Đồ Điều Trị Y Tế
100% Tiếng Việt
"""

import streamlit as st
import os
import sys
import time
import pandas as pd
from datetime import datetime

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

from src.diagnosis_chain import run_diagnosis_chain, run_diagnosis_chain_stream
from src.llm_agent import answer_document_question_stream, transcribe_audio
from scripts.parse_docs import extract_text_from_pdf, extract_text_from_docx
from src.i18n import LANG
from src.docx_exporter import markdown_to_docx_bytes
from src.sample_cases import SAMPLE_CASE_BANK, CATEGORY_ORDER_ROW1, CATEGORY_ORDER_ROW2, get_random_case
from streamlit_mic_recorder import mic_recorder


# ── Cấu hình trang ────────────────────────────────────────
st.set_page_config(
    page_title="Trợ Lý AI Y Tế – Medical RAG",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Import font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    /* Header gradient - Clinical Teal/Blue */
    .main-header {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(2, 132, 199, 0.15);
    }
    .main-header h1 {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
    }
    .main-header p {
        color: rgba(255,255,255,0.85);
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Card styling */
    .info-card {
        background: linear-gradient(145deg, #f8fafc, #e2e8f0);
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.5rem 0;
    }
    
    /* Step indicators */
    .step-badge {
        display: inline-block;
        background: #0066CC;
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .step-badge.done {
        background: #16a34a;
    }
    .step-badge.running {
        background: #ea580c;
    }
    
    /* Result cards */
    .ddx-high { 
        border-left: 4px solid #dc2626; 
        padding-left: 1rem;
        margin: 0.5rem 0;
    }
    .ddx-medium { 
        border-left: 4px solid #f59e0b; 
        padding-left: 1rem;
        margin: 0.5rem 0;
    }
    .ddx-low { 
        border-left: 4px solid #22c55e; 
        padding-left: 1rem;
        margin: 0.5rem 0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%);
    }
    
    /* Safety blocked */
    .safety-blocked {
        background: #fef2f2;
        border: 2px solid #dc2626;
        border-radius: 12px;
        padding: 1.5rem;
    }
    
    /* Safety warning */
    .safety-warning {
        background: #fffbeb;
        border: 2px solid #f59e0b;
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Disclaimer */
    .disclaimer {
        background: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 8px;
        padding: 1rem;
        font-size: 0.85rem;
        color: #166534;
    }
    
    /* Hide Streamlit default */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #0284c7, #0369a1);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s ease;
        box-shadow: 0 4px 6px rgba(2, 132, 199, 0.2);
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 12px rgba(2, 132, 199, 0.3);
        background: linear-gradient(135deg, #0369a1, #075985);
    }
    
    /* Input titles */
    .input-label {
        font-weight: 600;
        color: #334155;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Lấy từ điển ngôn ngữ hiện tại
t = LANG[st.session_state.get("lang", "vi")]

# ── Sidebar ────────────────────────────────────────────────
with st.sidebar:
        
    st.markdown(f"### 📊 {t['sidebar_info']}")
    st.markdown("""
    - **LLM:** Gemini 2.5 Flash
    - **RAG:** LangChain + ChromaDB
    - **Tìm kiếm:** Hybrid (Vector + BM25)
    - **An toàn:** SafetyGuardrail 
    - **Tri thức:** 3 phác đồ (424 chunks)
    """)
    
    st.divider()
    # ── Language Selector ──
    st.markdown("🌐 **Ngôn ngữ / Language**")
    selected_lang = st.radio("Select language:", ["Tiếng Việt", "English"], index=0 if st.session_state.get("lang", "vi") == "vi" else 1, label_visibility="collapsed")
    st.session_state.lang = "vi" if selected_lang == "Tiếng Việt" else "en"
    
    st.divider()
    
    # Session history
    st.markdown(f"### 📜 {t['sidebar_history']}")
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"Ca #{len(st.session_state.history) - i}: {entry['specialty']}", expanded=False):
                st.markdown(f"**{t['history_symptoms']}:** {entry['input'][:80]}...")
                st.markdown(f"**{t['history_time']}:** {entry['time']}")
    else:
        st.caption(t["no_recent_cases"])
    
    st.divider()
    st.markdown("""
    <div class="disclaimer">
    <strong>Tuyên bố miễn trách nhiệm:</strong> Công cụ này chỉ hỗ trợ tham khảo, 
    không thay thế phán đoán lâm sàng của bác sĩ.
    </div>
    """, unsafe_allow_html=True)


# ── Main Content ───────────────────────────────────────────

# Cập nhật lại t sau khi người dùng có thể thay đổi ngôn ngữ trong sidebar
t = LANG[st.session_state.get("lang", "vi")]

# Header
st.markdown(f"""
<div class="main-header">
    <h1>{t["app_title"]}</h1>
    <p>{t["app_subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([t["tab_rag"], t["tab_doc"], t["tab_dash"]])

# ==========================================
# TAB 1: Hệ thống RAG gốc
# ==========================================
with tab1:

    # ── Form nhập ca bệnh ─────────────────────────────────────
    # Bộ ca bệnh mẫu (Ngẫu nhiên)
    st.markdown(f"<p style='font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;'><b>{t['demo_cases']}</b></p>", unsafe_allow_html=True)
    
    # Khởi tạo các giá trị default vào session_state từ đầu vòng đời
    if "case_input" not in st.session_state:
        st.session_state.case_input = ""
    if "specialty" not in st.session_state:
        st.session_state.specialty = "Tự động nhận diện"
    if "age" not in st.session_state:
        st.session_state.age = 0
    if "sex" not in st.session_state:
        st.session_state.sex = t['sex_options'][0]

    # Callback load ca bệnh ngẫu nhiên từ ngân hàng
    def load_random_sample(category: str):
        case_data = get_random_case(category)
        st.session_state.case_input = case_data["text"]
        st.session_state.specialty = case_data["specialty"]
        st.session_state.age = case_data["age"]
        st.session_state.sex = case_data["sex"]
    
    # Render nút ca mẫu — Hàng 1: 3 ô đơn khoa
    row1_cols = st.columns(3)
    for idx, category in enumerate(CATEGORY_ORDER_ROW1):
        row1_cols[idx].button(
            category,
            on_click=load_random_sample,
            args=(category,),
            key=f"sample_r1_{idx}",
            use_container_width=True,
        )
    
    # Render nút ca mẫu — Hàng 2: 4 ô hỗn hợp
    row2_cols = st.columns(4)
    for idx, category in enumerate(CATEGORY_ORDER_ROW2):
        row2_cols[idx].button(
            category,
            on_click=load_random_sample,
            args=(category,),
            key=f"sample_r2_{idx}",
            use_container_width=True,
        )

    with st.container(border=True):
        st.markdown(f"<h3 style='margin-top:0; color:#0f172a;'>{t['clinical_info']}</h3>", unsafe_allow_html=True)
        
        case_input = st.text_area(
            t["symptoms_label"],
            height=130,
            placeholder=t["symptoms_placeholder"],
            key="case_input"
        )
        
        # 🎙️ Nút ghi âm giọng nói
        col_mic, col_status = st.columns([1, 4])
        with col_mic:
            audio = mic_recorder(
                start_prompt=t["voice_rec_label"],
                stop_prompt="⏹️",
                key='recorder',
                use_container_width=True
            )
        
        if audio:
            with col_status:
                with st.spinner(t["voice_processing"]):
                    transcribed_text = transcribe_audio(audio['bytes'], language_instruction=t["prompt_instruction"])
                    if transcribed_text and "[Không nghe rõ" not in transcribed_text:
                        # Append to current input
                        if st.session_state.case_input:
                            st.session_state.case_input += " " + transcribed_text
                        else:
                            st.session_state.case_input = transcribed_text
                        st.rerun()
                    elif "[Không nghe rõ" in transcribed_text:
                        st.warning(transcribed_text)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            specialty_opts = [t["auto_detect_specialty"], t["cardiology"], t["respiratory"], t["endocrinology"]]
            specialty = st.selectbox(t["specialty_label"], specialty_opts, key="specialty")
        with col_b:
            age = st.number_input(t["age_label"], min_value=0, max_value=120, key="age")
        with col_c:
            sex = st.selectbox(t["sex_label"], t["sex_options"], key="sex")
        
        # Thêm thông tin vào input nếu có
        enriched_input = case_input
        if age > 0:
            enriched_input = f"Bệnh nhân {age} tuổi. {enriched_input}"
        if sex != t["unspecified_sex"]:
            enriched_input = f"Giới tính: {sex}. {enriched_input}"
            
        # Xác định chuyên khoa
        selected_specialty = None if specialty == t["auto_detect_specialty"] else specialty
        
        # ── Nút phân tích ─────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_clicked = st.button(t['btn_analyze'], type="primary")
    
    # ── Xử lý phân tích khi nhấn nút ─────────────────────────
    if analyze_clicked:
        if not case_input.strip():
            st.error(t["error_empty_input"])
        elif not os.getenv("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY") == "your_api_key_here":
            st.error(t["error_api_key"])
        else:
            st.divider()
            st.markdown(f"## 📊 {t['analysis_results']}")
            
            # Streaming output
            with st.spinner(t.get('step_analysis', "Đang chuẩn bị...")):
                # Containers cho mỗi bước
                progress_bar = st.progress(5, text="Khởi động quá trình phân tích...")
                step3_container = st.container()
                step4_container = st.container()
                
                # Chạy chain streaming
                ddx_text_buffer = ""
                summary_text_buffer = ""
                drug_warning_buffer = ""
                step3_text_placeholder = None
                step4_text_placeholder = None
                
                for event in run_diagnosis_chain_stream(enriched_input, selected_specialty, language_instruction=t["prompt_instruction"]):
                    step = event['step']
                    content = event['content']
                    
                    if step == "blocked":
                        st.markdown(f'<div class="safety-blocked">{content}</div>', unsafe_allow_html=True)
                        break
                    
                    elif step == "warning":
                        st.markdown(f'<div class="safety-warning">{content}</div>', unsafe_allow_html=True)
                    
                    elif step == "step1_start":
                        progress_bar.progress(15, text=t.get('step_analysis', "Đang phân tích ca bệnh..."))
                    
                    elif step == "step1_done":
                        pass
                    
                    elif step == "step2_start":
                        progress_bar.progress(35, text=t.get('step_search', "Đang tra cứu phác đồ..."))
                    
                    elif step == "step2_done":
                        pass
                    
                    elif step == "step3_start":
                        progress_bar.progress(55, text=t.get('step_ddx', "Đang lập luận chẩn đoán phân biệt..."))
                        with step3_container:
                            st.markdown(f"### 🧠 {t['ddx_title']}")
                            step3_text_placeholder = st.empty()
                    
                    elif step == "step3_stream":
                        ddx_text_buffer += content
                        if step3_text_placeholder:
                            step3_text_placeholder.markdown(ddx_text_buffer)
                    
                    elif step == "step3_done":
                        if step3_text_placeholder:
                            step3_text_placeholder.markdown(ddx_text_buffer)
                    
                    elif step == "step4_start":
                        progress_bar.progress(85, text="Đang tổng hợp khuyến nghị...")
                        with step4_container:
                            st.markdown(f"### 📝 {t['summary_title']}")
                            step4_text_placeholder = st.empty()
                    
                    elif step == "step4_stream":
                        summary_text_buffer += content
                        if step4_text_placeholder:
                            step4_text_placeholder.markdown(summary_text_buffer)
                    
                    elif step == "step4_done":
                        if step4_text_placeholder:
                            step4_text_placeholder.markdown(summary_text_buffer)
                    
                    elif step == "drug_warning":
                        drug_warning_buffer = content
                        if "[Không phát hiện" not in content and "No serious drug interactions" not in content:
                            st.warning(f"### {t['drug_warning_title']}\n\n{content}")
                        else:
                            st.info(f"💡 {t['no_drug_warning']}")
                    
                    elif step == "complete":
                        progress_bar.progress(100, text=t.get('result_success', "Hoàn thành!"))
                        time.sleep(0.5)
                        progress_bar.empty()
                        st.success(t["result_success"])
                        
                        # Lưu lịch sử
                        st.session_state.history.append({
                            'input': case_input[:100],
                            'specialty': selected_specialty or t["auto_detect_specialty_short"],
                            'time': datetime.now().strftime("%H:%M %d/%m"),
                            'ddx': ddx_text_buffer[:200]
                        })
                
                # Lưu kết quả vào session_state để giữ kết quả khi nhấn nút tải xuống
                if ddx_text_buffer:
                    full_report = f"""# 📋 {t['report_title']}
**{t['report_specialty']}:** {selected_specialty or t['auto_detect_specialty_short']}

## 🏥 {t['report_case_info']}
{enriched_input}

## 🧠 {t['report_ddx']}
{ddx_text_buffer}

## 📝 {t['report_summary']}
{summary_text_buffer}

---
⚕️ *{t['disclaimer']}*
"""
                    st.session_state.last_result = {
                        'ddx_text': ddx_text_buffer,
                        'summary_text': summary_text_buffer,
                        'drug_warning': drug_warning_buffer,
                        'full_report': full_report,
                        'enriched_input': enriched_input,
                        'selected_specialty': selected_specialty,
                    }
    
    # ── Hiển thị kết quả (từ session_state nếu không phải lần chạy phân tích) ──
    if st.session_state.get('last_result'):
        result = st.session_state.last_result
        
        # Nếu không phải vừa bấm nút phân tích (trong lúc stream đã hiện rồi) thì in lại từ cache
        if not analyze_clicked:
            st.divider()
            st.markdown(f"## 📊 {t['analysis_results']}")
            
            # Khôi phục cảnh báo thuốc nếu có
            if result.get('drug_warning'):
                warning_content = result['drug_warning']
                if "[Không phát hiện" not in warning_content and "No serious drug interactions" not in warning_content:
                    st.warning(f"### {t['drug_warning_title']}\n\n{warning_content}")
                else:
                    st.info(f"💡 {t['no_drug_warning']}")
            
            with st.container():
                st.markdown(f"### 🧠 {t['ddx_title']}")
                st.markdown(result['ddx_text'])
            with st.container():
                st.markdown(f"### 📝 {t['summary_title']}")
                st.markdown(result['summary_text'])
                
        st.divider()
        
        # ── Nút xuất báo cáo ──
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button(
                label=t["btn_dl_md"],
                data=result['full_report'],
                file_name=f'bao_cao_cdpb_{datetime.now().strftime("%Y%m%d_%H%M")}.md',
                mime='text/markdown',
                use_container_width=True
            )
        with col_dl2:
            try:
                docx_bytes = markdown_to_docx_bytes(result['full_report'], title=t["report_title_short"])
                st.download_button(
                    label=t.get("btn_dl_docx", "📥 Tải Báo Cáo (DOCX)"),
                    data=docx_bytes,
                    file_name=f'bao_cao_cdpb_{datetime.now().strftime("%Y%m%d_%H%M")}.docx',
                    mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Lỗi tạo DOCX: {e}")

# ==========================================
# TAB 2: Phân tích Tài liệu (Upload & Q&A) – Hỗ trợ nhiều file
# ==========================================
with tab2:
    with st.container(border=True):
        st.markdown(f"<h3 style='margin-top:0; color:#0f172a;'>{t['doc_upload_title']}</h3>", unsafe_allow_html=True)
        st.info(t["doc_upload_info"])
        
        uploaded_files = st.file_uploader(
            t["doc_upload_label"],
            type=["pdf", "docx"],
            accept_multiple_files=True
        )
    
    # Session state variables cho Tab 2
    if "doc_content" not in st.session_state:
        st.session_state.doc_content = ""
    if "doc_names" not in st.session_state:
        st.session_state.doc_names = []
    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []
        
    if uploaded_files:
        # Lấy danh sách tên file hiện tại
        current_file_names = sorted([f.name for f in uploaded_files])
        prev_file_names = sorted(st.session_state.doc_names)
        
        # Nếu danh sách file thay đổi -> xử lý lại
        if current_file_names != prev_file_names:
            with st.spinner(t["doc_reading"]):
                all_texts = []
                file_info_list = []
                
                for uploaded_file in uploaded_files:
                    file_extension = uploaded_file.name.split('.')[-1].lower()
                    
                    # Ghi file tạm để thư viện đọc
                    temp_path = f"temp_upload_{uploaded_file.name}"
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Trích xuất text
                    if file_extension == "pdf":
                        text_content = extract_text_from_pdf(temp_path)
                    else:
                        text_content = extract_text_from_docx(temp_path)
                    
                    # Clean up
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                    
                    all_texts.append(f"\n\n--- [{uploaded_file.name}] ---\n\n{text_content}")
                    file_info_list.append(f"• **{uploaded_file.name}** ({len(text_content):,} {t['characters']})")
                
                st.session_state.doc_content = "\n".join(all_texts)
                st.session_state.doc_names = current_file_names
                st.session_state.qa_history = []  # Reset lịch sử chat
        
        # Hiển thị thông tin các file đã tải
        total_chars = len(st.session_state.doc_content)
        num_files = len(st.session_state.doc_names)
        st.success(f"✅ {t['doc_multi_loaded']} **{num_files}** {t['doc_files_count']} ({total_chars:,} {t['doc_total_chars']})")
        
        if num_files > 1:
            with st.expander(f"📂 Danh sách {num_files} file", expanded=False):
                for fname in st.session_state.doc_names:
                    st.markdown(f"• {fname}")
        
        # Phần giao diện Chat
        st.divider()
        st.markdown(f"### 💬 {t['doc_chat_title']}")
        
        # Hiển thị lịch sử chat
        for message in st.session_state.qa_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
        # Khung nhập chat mới
        if user_question := st.chat_input(t["doc_chat_placeholder"]):
            if not os.getenv("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY") == "your_api_key_here":
                st.error(t["error_api_key"])
            else:
                # Add user message to UI
                st.chat_message("user").markdown(user_question)
                # Lưu vào lịch sử
                st.session_state.qa_history.append({"role": "user", "content": user_question})
                
                # Gọi AI trả lời
                with st.chat_message("assistant"):
                    response_placeholder = st.empty()
                    full_response = ""
                    
                    try:
                        # Rút gọn context nếu quá dài (tránh vỡ token limit)
                        context_to_send = st.session_state.doc_content[:150000] 
                        
                        for chunk in answer_document_question_stream(context_to_send, user_question, language_instruction=t["prompt_instruction"]):
                            full_response += chunk
                            response_placeholder.markdown(full_response + "▌")
                            
                        response_placeholder.markdown(full_response)
                        # Lưu lịch sử
                        st.session_state.qa_history.append({"role": "assistant", "content": full_response})
                    except Exception as e:
                        error_msg = f"❌ {t['error_occurred']}: {e}"
                        response_placeholder.error(error_msg)
                        st.session_state.qa_history.append({"role": "assistant", "content": error_msg})

# ==========================================
# TAB 3: Dashboard & Thống Kê
# ==========================================
with tab3:
    st.markdown(f"## 📊 {t['dash_title']}")
    st.markdown(t['dash_desc'])
    
    # Tính toán Metrics
    total_cases = len(st.session_state.history)
    
    # Dummy data nếu chưa có thật để demo đẹp
    history_data = st.session_state.history.copy()
    if len(history_data) == 0:
        history_data = [
            {"specialty": t["cardiology"], "time": "08:15 10/03", "input": "Bệnh nhân nhịp chậm 40 l/p, HA 85/50...", "ddx": "Suy tim cấp"},
            {"specialty": t["endocrinology"], "time": "09:30 10/03", "input": "Đường huyết đói 7.5, HbA1c 6.8...", "ddx": "Đái tháo đường T2"},
            {"specialty": t["respiratory"], "time": "10:45 10/03", "input": "Khó thở mMRC 2, tiền sử 2 đợt cấp COPD...", "ddx": "COPD Nhóm D"}
        ]
        
    df = pd.DataFrame(history_data)
    
    # ── Metrics Row ──
    met1, met2, met3 = st.columns(3)
    with met1:
        st.metric(label=t["dash_total"], value=total_cases if total_cases > 0 else 3)
    with met2:
        st.metric(label=t["dash_data"], value="424 Chunks", delta="3 Protocols")
    with met3:
        st.metric(label=t["dash_speed"], value="1.2s", delta="-0.3s")
    st.divider()
    
    # ── Charts Row ──
    chart_col, data_col = st.columns([1, 1.5])
    
    with chart_col:
        st.markdown(f"### {t['chart_title']}")
        if not df.empty and "specialty" in df.columns:
            spec_counts = df["specialty"].value_counts()
            st.bar_chart(spec_counts, color="#0284c7")
        else:
            st.info(t["insufficient_data"])
            
    with data_col:
        st.markdown(f"### {t['table_title']}")
        if not df.empty:
            st.dataframe(
                df[["time", "specialty", "input"]], 
                use_container_width=True,
                column_config={
                    "time": "Thời gian",
                    "specialty": "Chuyên khoa",
                    "input": "Nội dung Input"
                }
            )
        else:
            st.info(t["no_cases_yet"])
            
    st.divider()
    if not df.empty:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=t["btn_export_csv"],
            data=csv,
            file_name=f'clinical_history_{datetime.now().strftime("%Y%m%d")}.csv',
            mime='text/csv',
        )

# ── Footer disclaimer ─────────────────────────────────────
st.divider()
st.markdown(f"""
<div class="disclaimer" style="text-align: center;">
    ⚕️ {t['footer_text']}
</div>
""", unsafe_allow_html=True)
