"""
llm_agent.py – Gemini 2.5 Flash Wrapper
Sử dụng google-genai SDK (phiên bản mới)
"""

import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# ── Cấu hình ──────────────────────────────────────────────
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.3
MAX_OUTPUT_TOKENS = 8192


def get_client() -> genai.Client:
    """Khởi tạo Gemini client."""
    return genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_response(prompt: str, temperature: float = TEMPERATURE) -> str:
    """
    Gọi Gemini API và trả về response text.
    Có retry logic tối đa 3 lần.
    """
    client = get_client()
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                )
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** (attempt + 1)
                print(f"⚠️ Lỗi API (lần {attempt + 1}): {e}. Thử lại sau {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise Exception(f"❌ Lỗi API sau {max_retries} lần thử: {e}")


def generate_response_stream(prompt: str, temperature: float = TEMPERATURE):
    """
    Gọi Gemini API với streaming response.
    Yields từng phần text.
    """
    client = get_client()
    
    try:
        response = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=MAX_OUTPUT_TOKENS,
            )
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"\n\n❌ Lỗi khi tạo phản hồi: {e}"


# ── Drug Interaction Prompt ─────────────────────────────

DRUG_INTERACTION_PROMPT = """Bạn là dược sĩ lâm sàng chuyên nghiệp. Hãy kiểm tra các tương tác thuốc và cảnh báo an toàn thuốc cho ca bệnh sau.
{language_instruction}

**Thông tin ca bệnh:**
{case_input}

**Các thuốc được đề cập (nếu có):**
{medications}

**Nội dung tra cứu từ phác đồ:**
{retrieved_context}

**Yêu cầu:** 
1. Liệt kê các tương tác thuốc-thuốc hoặc thuốc-bệnh lý tiềm tàng.
2. Đưa ra cảnh báo về liều lượng hoặc chống chỉ định nếu có trong phác đồ.
3. Nếu không có tương tác nào đáng ngại, hãy trả lời: "Không phát hiện tương tác thuốc nghiêm trọng."
4. KHÔNG tự bịa ra tương tác nếu không có bằng chứng y khoa.

Trả lời ngắn gọn, tập trung vào an toàn."""

CASE_ANALYSIS_PROMPT = """Bạn là trợ lý AI hỗ trợ lâm sàng. Hãy phân tích ca bệnh sau và trích xuất thông tin có cấu trúc.
{language_instruction}

**Ca bệnh:**
{case_input}

**Hãy trích xuất:**
1. Triệu chứng chính (Chief Complaint)
2. Tuổi / Giới tính
3. Các triệu chứng kèm theo
4. Yếu tố nguy cơ
5. Tiền sử bệnh
6. Chuyên khoa liên quan nhất (Tim mạch / Hô hấp / Nội tiết - Chuyển hóa)
7. Các từ khóa y tế để tra cứu phác đồ

Định dạng rõ ràng."""


DIFFERENTIAL_DIAGNOSIS_PROMPT = """Bạn là bác sĩ chuyên khoa đang hỗ trợ chẩn đoán phân biệt. 
Dựa vào thông tin ca bệnh và các đoạn phác đồ y tế Việt Nam được cung cấp bên dưới,
hãy lập danh sách chẩn đoán phân biệt có xếp hạng.
{language_instruction}

**Thông tin ca bệnh đã phân tích:**
{case_analysis}

**Phác đồ y tế liên quan (từ Bộ Y tế Việt Nam):**
{retrieved_context}

---

**Yêu cầu:** Lập danh sách chẩn đoán phân biệt với format sau cho MỖI chẩn đoán:

### [Số thứ tự]. [Tên bệnh] — Khả năng: [CAO / TRUNG BÌNH / THẤP]

**Bằng chứng ủng hộ:**
- [Liệt kê các triệu chứng, yếu tố từ ca bệnh phù hợp]

**Bằng chứng phản đối:**
- [Liệt kê các yếu tố không phù hợp, nếu có]

**Cận lâm sàng đề xuất:**
- [Xét nghiệm, chẩn đoán hình ảnh cần làm]

**Nguồn phác đồ tham chiếu:**
- [Trích dẫn tên tài liệu phác đồ đã sử dụng]

---

Lưu ý quan trọng:
- Xếp hạng từ khả năng CAO đến THẤP
- **KHÔNG BAE GIỜ** in ra tên file raw (VD: `tieuduong_type2_byt_2020.pdf`). Thay vì vậy, luôn BẮT BUỘC phiên dịch tên file thành tên tài liệu dễ đọc, chuyên nghiệp (VD: "Hướng dẫn chẩn đoán và điều trị Hô hấp, Bộ Y Tế", "Phác đồ đái tháo đường típ 2, Bộ Y tế 2020").
- Luôn trích dẫn nguồn phác đồ cụ thể theo định dạng mượt mà (VD: "Theo Phác đồ ĐTĐ Bộ Y Tế 2020, mục 5.a...")
- Chỉ sử dụng thông tin từ phác đồ y tế được cung cấp, KHÔNG tự bịa thêm
- Nếu không đủ thông tin để chẩn đoán, hãy nói rõ
- QUAN TRỌNG: Luôn bám sát nội dung phác đồ được cung cấp. Khi trích dẫn tiêu chuẩn chẩn đoán, phải ghi rõ TỪNG điều kiện kèm theo (ví dụ: điều kiện về triệu chứng, yêu cầu xét nghiệm lặp lại, ngoại lệ, chống chỉ định...) theo đúng nguyên văn tài liệu. Nếu ca bệnh đáp ứng đủ điều kiện thì kết luận, nếu thiếu thì nêu rõ điều kiện nào còn thiếu."""


REPORT_SUMMARY_PROMPT = """Dựa trên kết quả chẩn đoán phân biệt sau, hãy tạo phần TÓM TẮT ngắn gọn
và KHUYẾN NGHỊ cho bác sĩ điều trị.
{language_instruction}

**Kết quả CĐPB:**
{ddx_result}

**Hãy tạo:**
1. **Tóm tắt** (2-3 câu): Tổng hợp ngắn gọn các chẩn đoán chính
2. **Ưu tiên xử trí**: Chẩn đoán nào cần xử trí/loại trừ trước nhất và tại sao
3. **Cận lâm sàng ưu tiên**: Top 3-5 xét nghiệm/thăm dò cần thực hiện ngay
4. **Cảnh báo** (nếu có): Dấu hiệu nguy hiểm cần theo dõi sát

Ngắn gọn, thực tiễn lâm sàng."""


DOCUMENT_QA_PROMPT = """Bạn là một chuyên gia phân tích tài liệu y khoa.
Nhiệm vụ của bạn là trả lời các câu hỏi dựa trên nội dung của văn bản phác đồ điều trị được cung cấp dưới đây.
{language_instruction}

**Nội dung tài liệu được trích xuất:**
--- BẮT ĐẦU TÀI LIỆU ---
{document_context}
--- KẾT THÚC TÀI LIỆU ---

**Câu hỏi của người dùng:**
{question}

**Yêu cầu:**
1. Trả lời chi tiết, chính xác và 100% dựa trên nội dung tài liệu được cung cấp.
2. Nhanh chóng đưa ra kết luận (nếu có) trước khi giải thích chi tiết.
3. Nếu tài liệu không chứa thông tin để trả lời câu hỏi, hãy nói rõ: "Xin lỗi, văn bản này không đề cập đến thông tin bạn cần." KHÔNG tự suy đoán bên ngoài.
4. Trả lời chuyên nghiệp, sử dụng markdown để làm nổi bật (in đậm, in nghiêng) các điểm cốt lõi.
"""

def transcribe_audio(audio_bytes: bytes, language_instruction: str = "") -> str:
    """
    Sử dụng Gemini để chuyển đổi âm thanh y khoa thành văn bản.
    """
    client = get_client()
    
    # Prompt cho việc STT y khoa
    stt_prompt = f"""Bạn là chuyên gia thư ký y khoa. Hãy nghe kỹ đoạn âm thanh này và chuyển nó thành văn bản (transcription).
{language_instruction}
Yêu cầu:
1. Ghi lại chính xác các thuật ngữ y tế, tên thuốc, liều lượng.
2. Sửa các lỗi phát âm rõ ràng nhưng giữ nguyên ý nghĩa lâm sàng.
3. Trả về DUY NHẤT nội dung văn bản đã được chuyển đổi.
4. Nếu không có tiếng người hoặc không nghe rõ, hãy trả về: "[Không nghe rõ nội dung y tế]"
    """
    
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                types.Part.from_bytes(data=audio_bytes, mime_type="audio/wav"),
                stt_prompt
            ],
            config=types.GenerateContentConfig(
                temperature=0.0, # Cần độ chính xác cao nhất
            )
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ Lỗi STT: {e}")
        return f"[Lỗi chuyển đổi giọng nói: {str(e)}]"

def answer_document_question_stream(context: str, question: str, language_instruction: str = "", temperature: float = 0.2):
    """
    Tạo phản hồi dạng stream cho Document Q&A feature.
    """
    full_prompt = DOCUMENT_QA_PROMPT.format(
        document_context=context, 
        question=question,
        language_instruction=language_instruction
    )
    return generate_response_stream(full_prompt, temperature)

