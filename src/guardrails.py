"""
guardrails.py – Safety Guardrail Node
Chặn các truy vấn nguy hại trước khi xử lý
"""

import re


# ── Danh sách từ khóa nguy hại (tiếng Việt + tiếng Anh) ──
HARMFUL_KEYWORDS = {
    # Tự gây hại (có dấu + không dấu)
    "tự tử", "tu tu", "tự sát", "tu sat",
    "muốn chết", "muon chet", "cách chết", "cach chet",
    "kết thúc cuộc sống", "ket thuc cuoc song",
    "suicide", "kill myself", "end my life",
    
    # Gây hại người khác
    "giết người", "giet nguoi", "đầu độc", "dau doc",
    "hãm hại", "ham hai", "gây thương tích", "gay thuong tich",
    "cách giết", "cach giet", "murder", "poison someone",
    
    # Chất độc
    "pha chế thuốc độc", "pha che thuoc doc",
    "tạo chất độc", "tao chat doc",
    "công thức thuốc độc", "cong thuc thuoc doc",
    "cách tạo chất độc", "cach tao chat doc",
    "create poison", "make poison",
    
    # Lạm dụng thuốc
    "lạm dụng thuốc", "lam dung thuoc",
    "cách sử dụng ma túy", "cach su dung ma tuy",
    "cách dùng thuốc để", "cach dung thuoc de",
    "drug abuse", "overdose method",
    "dùng thuốc gây nghiện", "dung thuoc gay nghien",
    "mua thuốc cấm", "mua thuoc cam",
    
    # Gây hại trẻ em
    "bạo hành trẻ em", "bao hanh tre em",
    "child abuse", "lạm dụng trẻ em", "lam dung tre em",
}

# Từ khóa cảnh báo (không chặn hoàn toàn nhưng thêm cảnh báo)
WARNING_KEYWORDS = {
    "quá liều", "overdose", "tác dụng phụ nghiêm trọng",
    "liều tối đa", "tương tác thuốc nguy hiểm",
}

# ── Phản hồi an toàn ──────────────────────────────────────
BLOCKED_RESPONSE_VI = """⛔ **Truy vấn bị từ chối vì lý do an toàn.**

Hệ thống phát hiện nội dung có thể liên quan đến hành vi gây hại. 
Công cụ này chỉ hỗ trợ tra cứu phác đồ điều trị y tế hợp pháp.

**Nếu bạn hoặc ai đó đang gặp nguy hiểm:**
- 🆘 Đường dây nóng tư vấn tâm lý: **1800 599 920** (miễn phí)
- 🏥 Liên hệ cơ sở y tế gần nhất hoặc gọi **115**
- 💬 Tổng đài tư vấn sức khỏe tâm thần: **1900 0027**

Vui lòng nhập lại với nội dung y tế hợp lệ."""

WARNING_RESPONSE_VI = """⚠️ **Lưu ý quan trọng:**

Truy vấn của bạn chứa nội dung y tế nhạy cảm. Hệ thống vẫn xử lý 
nhưng xin lưu ý:
- Mọi thông tin về liều lượng thuốc cần được bác sĩ xác nhận
- KHÔNG tự ý thay đổi liều lượng hoặc phác đồ điều trị
- Liên hệ bác sĩ điều trị nếu có bất kỳ thắc mắc nào

---

"""


class SafetyGuardrailNode:
    """
    Node kiểm tra an toàn cho truy vấn người dùng.
    
    Returns:
        dict với keys:
            - 'is_safe': bool
            - 'has_warning': bool
            - 'message': str (thông báo nếu bị chặn hoặc cảnh báo)
    """
    
    def __init__(self):
        self.harmful_keywords = HARMFUL_KEYWORDS
        self.warning_keywords = WARNING_KEYWORDS
    
    def check(self, query: str) -> dict:
        """
        Kiểm tra truy vấn có an toàn không.
        
        Args:
            query: Truy vấn người dùng
        
        Returns:
            dict: {'is_safe': bool, 'has_warning': bool, 'message': str}
        """
        query_lower = query.lower().strip()
        
        # Kiểm tra từ khóa nguy hại (CHẶN HOÀN TOÀN)
        for keyword in self.harmful_keywords:
            if keyword in query_lower:
                return {
                    'is_safe': False,
                    'has_warning': False,
                    'message': BLOCKED_RESPONSE_VI,
                    'matched_keyword': keyword,
                    'severity': 'BLOCKED'
                }
        
        # Kiểm tra từ khóa cảnh báo (CHO PHÉP + CẢNH BÁO)
        for keyword in self.warning_keywords:
            if keyword in query_lower:
                return {
                    'is_safe': True,
                    'has_warning': True,
                    'message': WARNING_RESPONSE_VI,
                    'matched_keyword': keyword,
                    'severity': 'WARNING'
                }
        
        # An toàn
        return {
            'is_safe': True,
            'has_warning': False,
            'message': '',
            'matched_keyword': None,
            'severity': 'SAFE'
        }


# Singleton instance
safety_guardrail = SafetyGuardrailNode()
