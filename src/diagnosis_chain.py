"""
diagnosis_chain.py – Chuỗi 4 bước chẩn đoán phân biệt
Bước 1: Phân tích ca bệnh
Bước 2: Truy vấn tri thức (RAG)
Bước 3: Lập luận chẩn đoán phân biệt
Bước 4: Tạo báo cáo tổng hợp
"""

from src.guardrails import safety_guardrail
from src.llm_agent import (
    generate_response,
    generate_response_stream,
    CASE_ANALYSIS_PROMPT,
    DIFFERENTIAL_DIAGNOSIS_PROMPT,
    REPORT_SUMMARY_PROMPT,
    DRUG_INTERACTION_PROMPT,
)
from src.rag_engine import retrieve_context, format_context
from src.report_generator import format_final_report


def run_diagnosis_chain(
    case_input: str,
    specialty: str = None,
    language_instruction: str = "",
    stream: bool = False
) -> dict:
    """
    Chạy chuỗi 4 bước chẩn đoán phân biệt.
    
    Args:
        case_input: Mô tả ca bệnh từ người dùng
        specialty: Chuyên khoa (Tim mạch / Hô hấp / Nội tiết - Chuyển hóa)
        stream: Có stream output hay không
    
    Returns:
        dict với keys:
            - 'success': bool
            - 'safety': dict (kết quả kiểm tra an toàn)
            - 'case_analysis': str (Bước 1)
            - 'retrieved_sources': list (Bước 2)
            - 'ddx_result': str (Bước 3)
            - 'summary': str (Bước 4)
            - 'final_report': str (Báo cáo hoàn chỉnh)
            - 'error': str (nếu có lỗi)
    """
    result = {
        'success': False,
        'safety': None,
        'case_analysis': '',
        'retrieved_sources': [],
        'retrieved_context_text': '',
        'ddx_result': '',
        'summary': '',
        'final_report': '',
        'error': ''
    }
    
    try:
        # ── Bước 0: Kiểm tra Safety Guardrail ──────────────
        safety_check = safety_guardrail.check(case_input)
        result['safety'] = safety_check
        
        if not safety_check['is_safe']:
            result['error'] = safety_check['message']
            return result
        
        # ── Bước 1: Phân tích ca bệnh ─────────────────────
        print("🔍 Bước 1: Phân tích ca bệnh...")
        case_prompt = CASE_ANALYSIS_PROMPT.format(
            case_input=case_input,
            language_instruction=language_instruction
        )
        case_analysis = generate_response(case_prompt, temperature=0.2)
        result['case_analysis'] = case_analysis
        
        # ── Bước 2: Truy vấn tri thức (RAG) ───────────────
        print("📚 Bước 2: Truy vấn tri thức y tế...")
        # Dùng cả case_input gốc và phân tích để tìm kiếm
        search_query = f"{case_input}\n{case_analysis}"
        
        documents = retrieve_context(
            query=search_query,
            specialty=specialty,
            k=5
        )
        result['retrieved_sources'] = [
            {
                'content': doc.page_content[:200] + "...",
                'source': doc.metadata.get('source', 'N/A'),
                'specialty': doc.metadata.get('specialty', 'N/A')
            }
            for doc in documents
        ]
        
        context_text = format_context(documents)
        result['retrieved_context_text'] = context_text
        
        # ── Bước 3: Chẩn đoán phân biệt ──────────────────
        print("🧠 Bước 3: Lập luận chẩn đoán phân biệt...")
        ddx_prompt = DIFFERENTIAL_DIAGNOSIS_PROMPT.format(
            case_analysis=case_analysis,
            retrieved_context=context_text,
            language_instruction=language_instruction
        )
        ddx_result = generate_response(ddx_prompt, temperature=0.3)
        result['ddx_result'] = ddx_result
        
        # ── Bước 3.5: Kiểm tra tương tác thuốc ──────────
        print("💊 Bước 3.5: Kiểm tra tương tác thuốc...")
        drug_prompt = DRUG_INTERACTION_PROMPT.format(
            case_input=case_input,
            medications=ddx_result, # Giả định ddx_result chứa các thuốc đề xuất
            retrieved_context=context_text,
            language_instruction=language_instruction
        )
        drug_warning = generate_response(drug_prompt, temperature=0.1)
        result['drug_warning'] = drug_warning
        
        # ── Bước 4: Tóm tắt & Khuyến nghị ────────────────
        print("📋 Bước 4: Tạo tóm tắt và khuyến nghị...")
        summary_prompt = REPORT_SUMMARY_PROMPT.format(
            ddx_result=ddx_result,
            language_instruction=language_instruction
        )
        summary = generate_response(summary_prompt, temperature=0.2)
        result['summary'] = summary
        
        # ── Tạo báo cáo hoàn chỉnh ───────────────────────
        warning_msg = safety_check.get('message', '') if safety_check.get('has_warning') else ''
        
        result['final_report'] = format_final_report(
            case_input=case_input,
            specialty=specialty,
            case_analysis=case_analysis,
            ddx_result=ddx_result,
            summary=summary,
            sources=result['retrieved_sources'],
            warning=warning_msg
        )
        
        result['success'] = True
        print("✅ Hoàn thành chuỗi chẩn đoán!")
        
    except Exception as e:
        result['error'] = f"❌ Lỗi trong quá trình xử lý: {str(e)}"
        print(result['error'])
    
    return result


def run_diagnosis_chain_stream(
    case_input: str,
    specialty: str = None,
    language_instruction: str = ""
):
    """
    Phiên bản streaming của chuỗi chẩn đoán.
    Yields từng phần kết quả để hiển thị realtime trên Streamlit.
    """
    try:
        # Bước 0: Safety Check
        safety_check = safety_guardrail.check(case_input)
        if not safety_check['is_safe']:
            yield {"step": "blocked", "content": safety_check['message']}
            return      
        
        if safety_check.get('has_warning'):
            yield {"step": "warning", "content": safety_check['message']}
        
        # Bước 1: Phân tích ca bệnh
        yield {"step": "step1_start", "content": "🔍 **Bước 1:** Đang phân tích ca bệnh..."}
        case_prompt = CASE_ANALYSIS_PROMPT.format(
            case_input=case_input,
            language_instruction=language_instruction
        )
        case_analysis = generate_response(case_prompt, temperature=0.2)
        yield {"step": "step1_done", "content": case_analysis}
        
        # Bước 2: RAG retrieval
        yield {"step": "step2_start", "content": "📚 **Bước 2:** Đang tra cứu phác đồ y tế..."}
        search_query = f"{case_input}\n{case_analysis}"
        documents = retrieve_context(query=search_query, specialty=specialty, k=5)
        context_text = format_context(documents)
        
        sources_info = [
            f"- {doc.metadata.get('source', 'N/A')} ({doc.metadata.get('specialty', '')})"
            for doc in documents
        ]
        yield {"step": "step2_done", "content": "\n".join(sources_info) if sources_info else "Không tìm thấy tài liệu liên quan."}
        
        # Bước 3: DDx (Không dùng stream để tránh gãy kết nối API)
        yield {"step": "step3_start", "content": "🧠 **Bước 3:** Đang lập luận chẩn đoán phân biệt..."}
        ddx_prompt = DIFFERENTIAL_DIAGNOSIS_PROMPT.format(
            case_analysis=case_analysis,
            retrieved_context=context_text,
            language_instruction=language_instruction
        )
        
        ddx_full = generate_response(ddx_prompt, temperature=0.3)
        yield {"step": "step3_stream", "content": ddx_full}
        yield {"step": "step3_done", "content": ddx_full}
        
        # Bước 3.5: Kiểm tra tương tác thuốc
        yield {"step": "step_drug_check", "content": "💊 **Bước 3.5:** Đang kiểm tra tương tác thuốc..."}
        drug_prompt = DRUG_INTERACTION_PROMPT.format(
            case_input=case_input,
            medications=ddx_full,
            retrieved_context=context_text,
            language_instruction=language_instruction
        )
        drug_warning = generate_response(drug_prompt, temperature=0.1)
        yield {"step": "drug_warning", "content": drug_warning}
        
        # Bước 4: Tóm tắt
        yield {"step": "step4_start", "content": "📋 **Bước 4:** Đang tạo tóm tắt và khuyến nghị..."}
        summary_prompt = REPORT_SUMMARY_PROMPT.format(
            ddx_result=ddx_full,
            language_instruction=language_instruction
        )
        
        summary_full = generate_response(summary_prompt, temperature=0.2)
        yield {"step": "step4_stream", "content": summary_full}
        yield {"step": "step4_done", "content": summary_full}
        yield {"step": "complete", "content": "✅ Hoàn thành!"}

    except Exception as e:
        # Bắt toàn bộ lỗi (như lỗi API rate limit, quota exceeded...)
        print(f"❌ Lỗi hệ thống: {str(e)}")
        yield {"step": "error", "content": "Rất tiếc! Đã có sự cố kết nối hoặc máy chủ đang bị quá tải. Vui lòng thử lại sau ít phút."}
