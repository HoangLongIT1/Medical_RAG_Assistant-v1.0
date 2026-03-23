"""
sample_cases.py – Ngân hàng ca bệnh mẫu ngẫu nhiên
Gồm 35 ca bệnh (5 ca/nhóm) được định dạng chuẩn Bệnh án Nội khoa Lâm sàng.
"""

import random

def format_case(case_data: dict) -> str:
    template = f"""Dưới đây là một **ca bệnh giả lập theo phong cách ghi nhận thực tế của bác sĩ lâm sàng**:

---

### 📝 **BỆNH ÁN NỘI KHOA – {case_data['specialty'].upper()}**

**Họ tên:** {case_data.get('name', 'Nguyễn Văn A')}
**Giới tính:** {case_data['sex']}
**Tuổi:** {case_data['age']}
**Nghề nghiệp:** {case_data.get('job', 'Tự do')}
**Ngày khám:** 23/03/2026

---

### **1. Lý do nhập viện**
{case_data['reason']}

---

### **2. Bệnh sử**
{case_data['history']}

---

### **3. Tiền sử**
{case_data['past_medical']}

---

### **4. Khám lâm sàng**
{case_data['clinical']}

---

### **5. Cận lâm sàng**
{case_data['subclinical']}

---

### **6. Câu hỏi / Xử trí lâm sàng**
{case_data['question']}
"""
    return template

# ══════════════════════════════════════════════════════════════
# NGÂN HÀNG CA BỆNH MẪU CẤU TRÚC — 7 NHÓM (5 CA / NHÓM)
# ══════════════════════════════════════════════════════════════

SAMPLE_CASE_BANK = {

    # ──────────────────────────────────────────────────────────
    # NHÓM 1: TIM MẠCH (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫀 Tim mạch": [
        {
            "name": "Trần Văn M", "age": 70, "sex": "Nam", "job": "Hưu trí", "specialty": "TIM MẠCH",
            "reason": "Nhịp tim chậm, khó thở khi nằm",
            "history": "- Đột ngột choáng váng, khó thở khi nằm, phải kê cao gối hoặc ngồi thở.",
            "past_medical": "- Suy tim HFrEF (EF 35%).\n- Đang dùng: Bisoprolol 5mg/ngày.",
            "clinical": "**Sinh hiệu:** HA 85/50 mmHg, Mạch 40 lần/phút, SpO2 92%.\n**Lâm sàng:** Tay chân lạnh ẩm. Thở co kéo nhẹ, ran ẩm 2 đáy phổi.",
            "subclinical": "- **ECG:** Block nhĩ thất độ III.\n- **NT-proBNP:** 5800 pg/mL.",
            "question": "👉 Hướng xử trí cấp cứu huyết động và xử lý nhịp rớt do thuốc chẹn beta?"
        },
        {
            "name": "Lê Thị H", "age": 62, "sex": "Nữ", "job": "Nội trợ", "specialty": "TIM MẠCH",
            "reason": "Đau ngực trái dữ dội",
            "history": "- Đột ngột đau thắt ngực trái dữ dội lan hàm và vai trái kéo dài 45 phút, kèm vã mồ hôi hột.",
            "past_medical": "- Tăng HA 10 năm.\n- Dị ứng Aspirin (phù mạch).",
            "clinical": "**Sinh hiệu:** HA 160/95 mmHg, Mạch 95 lần/phút, SpO2 96%.\n**Lâm sàng:** Vã mồ hôi nhiều. T1 T2 rõ, không âm thổi.",
            "subclinical": "- **ECG:** ST chênh lên ở DII, DIII, aVF (NMCT thành dưới).\n- **Troponin T hs:** 250 ng/L.",
            "question": "👉 Chẩn đoán STEMI thành dưới. Kế hoạch dùng kháng kết tập tiểu cầu thay thế khi dị ứng Aspirin trước chụp mạch vành (PCI)?"
        },
        {
            "name": "Hoàng Văn K", "age": 55, "sex": "Nam", "job": "Kế toán", "specialty": "TIM MẠCH",
            "reason": "Đánh trống ngực, hồi hộp từng cơn",
            "history": "- 3 tháng nay hồi hộp rải rác 1-2 lần/tuần, kéo dài 30 phút, chóng mặt nhẹ.",
            "past_medical": "- Tăng huyết áp 5 năm (Enalapril 10mg).",
            "clinical": "**Sinh hiệu:** HA 140/85 mmHg, Mạch 82 lần/phút.\n**Lâm sàng:** Loạn nhịp hoàn toàn, T1 rõ.",
            "subclinical": "- **ECG:** Rung nhĩ đáp ứng thất trung bình.\n- **Siêu âm tim:** Nhĩ trái giãn 42mm, không huyết khối.",
            "question": "👉 Tính điểm CHA2DS2-VASc và đưa ra chỉ định dùng thuốc kháng đông đường uống (NOAC)?"
        },
        {
            "name": "Nguyễn Thị N", "age": 48, "sex": "Nữ", "job": "Văn phòng", "specialty": "TIM MẠCH",
            "reason": "Huyết áp cao phát hiện tình cờ",
            "history": "- Đo khám sức khỏe định kỳ thấy HA cao liên tiếp 3 ngày.",
            "past_medical": "- Yếu tố nguy cơ: Mẹ đột quỵ năm 60 tuổi, béo phì (BMI 34).",
            "clinical": "**Sinh hiệu:** HA trung bình 152/96 mmHg, Mạch 78 lần/phút.\n**Lâm sàng:** Không phù, tim nhịp đều.",
            "subclinical": "- **Sinh hóa:** Chol 6.5, LDL 4.2. Creatinin 1.0.\n- **ECG:** Dày thất trái (Sokolow-Lyon 38mm).",
            "question": "👉 Phân tầng nguy cơ tĩnh mạch và chỉ định phối hợp thuốc hạ áp bậc 1?"
        },
        {
            "name": "Trương Văn C", "age": 75, "sex": "Nam", "job": "Hưu trí", "specialty": "TIM MẠCH",
            "reason": "Phù chân, tiểu ít",
            "history": "- Phù tăng dần 2 chân 1 tuần, khó thở khi gắng sức nhẹ, cân tăng 4kg.",
            "past_medical": "- Suy tim mạn tính EF 28%, Rung nhĩ vĩnh viễn (dùng Furosemide, Spironolactone).",
            "clinical": "**Sinh hiệu:** HA 100/65 mmHg, Mạch 55 lần/phút.\n**Lâm sàng:** Tĩnh mạch cổ nổi, gan to 3cm, phù mềm ấn lõm, ran ẩm đáy phổi.",
            "subclinical": "- **Điện giải:** Na 128 mEq/L, K 5.6 mEq/L.\n- **Thận:** Creatinin 2.1 mg/dL (tăng).",
            "question": "👉 Đợt cấp suy tim mạn có suy thận cấp & rối loạn điện giải do thuốc. Hướng điều chỉnh thuốc lợi tiểu và men chuyển?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 2: HÔ HẤP (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫁 Hô hấp": [
        {
            "name": "Phạm Văn T", "age": 58, "sex": "Nam", "job": "Công nhân", "specialty": "HÔ HẤP",
            "reason": "Khó thở dữ dội, khạc đờm mủ xanh",
            "history": "- Ho tăng dần 3 ngày, đờm xanh, sốt 38.5°C, khó thở liên tục phải ngồi thở.",
            "past_medical": "- COPD 8 năm (FEV1 38%). Thường xuyên có đợt cập (2 lần/năm).",
            "clinical": "**Sinh hiệu:** HA 130/80 mmHg, Mạch 105 l/p, Nhịp thở 28 l/p, SpO2 86%.\n**Lâm sàng:** Co kéo cơ hô hấp phụ, phổi ran rít, ran nổ.",
            "subclinical": "- **Khí máu:** pH 7.32, PaCO2 58 mmHg, PaO2 52 mmHg (Toan hô hấp).\n- **X-quang:** Thâm nhiễm đáy phổi trái.",
            "question": "👉 Xử trí cấp cứu Đợt cấp COPD nặng: Chỉ định thở máy không xâm lấn (NIV) và phác đồ kháng sinh kinh nghiệm?"
        },
        {
            "name": "Nguyễn Thị L", "age": 45, "sex": "Nữ", "job": "Giáo viên", "specialty": "HÔ HẤP",
            "reason": "Ho khan kéo dài, khò khè về đêm",
            "history": "- Ho khan 6 tuần, nặng về rạng sáng hoặc gặp lạnh. Nghe tiếng rít khi thở.",
            "past_medical": "- Viêm mũi dị ứng mạn tính.",
            "clinical": "**Sinh hiệu:** Sinh hiệu ổn định, SpO2 98%.\n**Lâm sàng:** Phổi rải rác ran rít nhỏ cuối thì thở ra.",
            "subclinical": "- **Hô hấp ký:** Test phục hồi phế quản (+): FEV1 tăng 15%.\n- **FeNO:** 45 ppb.",
            "question": "👉 Chẩn đoán Hen phế quản. Khuyến cáo bậc điều trị kiểm soát hen theo GINA?"
        },
        {
            "name": "Trần Thị D", "age": 72, "sex": "Nữ", "job": "Hưu trí", "specialty": "HÔ HẤP",
            "reason": "Khó thở đột ngột, đau ngực hít sâu",
            "history": "- Đột nhiên khó thở dữ dội, đau nhói ngực bên phải khi hít thở rạng sáng nay.",
            "past_medical": "- Thay khớp háng 10 ngày trước, bất động tại giường. Béo phì.",
            "clinical": "**Sinh hiệu:** HA 100/70 mmHg, Mạch 110 l/p, Nhịp thở 26 l/p, SpO2 90%.\n**Lâm sàng:** Chân phải sưng to. Phổi trong.",
            "subclinical": "- **D-dimer:** > 5000 ng/mL.\n- **ECG:** S1Q3T3.\n- **Khí máu:** PaO2 62 mmHg, PaCO2 30 mmHg.",
            "question": "👉 Đánh giá Thuyên tắc phổi theo thang điểm Wells và chỉ định chẩn đoán hình ảnh khẩn cấp?"
        },
        {
            "name": "Đặng Văn S", "age": 35, "sex": "Nam", "job": "Lao động tự do", "specialty": "HÔ HẤP",
            "reason": "Ho đờm trắng, sốt chiều, sụt cân",
            "history": "- Ho khạc đờm 1 tháng, mồ hôi trộm, sốt 37.5 - 38 chiều mụn. Sụt 4kg.",
            "past_medical": "- Từng có người ghép cùng phòng trọ mắc lao.",
            "clinical": "**Sinh hiệu:** Ổn định.\n**Lâm sàng:** Hội chứng nhiễm trùng mạn, thể trạng gầy. Ran nổ đỉnh phổi phải.",
            "subclinical": "- **X-quang ngực:** Thâm nhiễm kèm dạng hang nhỏ ở đỉnh phổi phải.\n- **Máu:** Bạch cầu 9500 (Lympho 35%), CRP 35, VS 55mm/h.",
            "question": "👉 Nghi ngờ Lao phổi (TB). Chỉ định ngay xét nghiệm đờm (AFB/Xpert) và phác đồ điều trị hệ thống nếu dương tính?"
        },
        {
            "name": "Lương Thu Th", "age": 60, "sex": "Nữ", "job": "Nội trợ", "specialty": "HÔ HẤP",
            "reason": "Khó thở mạn tính, rát họng",
            "history": "- Khó thở tăng khi đi bộ (mMRC 2), ho khạc đờm buổi sáng. Cơn cấp 2 lần/năm.",
            "past_medical": "- Hút thuốc 30 gói-năm (đã bỏ 2 năm).",
            "clinical": "**Sinh hiệu:** Hơi thở nhanh 22 l/p, SpO2 94%.\n**Lâm sàng:** Lồng ngực dạng thùng, rì rào phế nang giảm.",
            "subclinical": "- **Hô hấp ký:** FEV1/FVC = 0.58, FEV1 42% sau giãn phế quản.\n- **X-quang:** Khí phế thũng.",
            "question": "👉 Theo phân nhóm mức độ COPD GOLD, bệnh nhân thuộc nhóm nào và chỉ định thuốc hít cắt cơn/duy trì?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 3: NỘI TIẾT (5 CA)
    # ──────────────────────────────────────────────────────────
    "🔬 Nội tiết": [
        {
            "name": "Bùi Văn P", "age": 45, "sex": "Nam", "job": "Kinh doanh", "specialty": "NỘI TIẾT",
            "reason": "Đường huyết cao khi khám định kỳ",
            "history": "- Không triệu chứng (ăn nhiều, uống nhiều, tiểu nhiều). Cảm thấy hoàn toàn khỏe mạnh.",
            "past_medical": "- Bố bị ĐTĐ type 2. BMI 27.5 (Thừa cân).",
            "clinical": "**Sinh hiệu:** HA 135/85 mmHg.\n**Lâm sàng:** Béo bụng eo 96 cm, gai đen vùng cổ.",
            "subclinical": "- **FPG (Đường đói):** Lần 1: 7.5, Lần 2: 7.8 mmol/L.\n- **HbA1c:** 6.8%.",
            "question": "👉 Tiêu chuẩn chẩn đoán chuẩn ĐTĐ Type 2. Phác đồ khởi trị thay đổi lối sống kết hợp Metformin?"
        },
        {
            "name": "Lê Vũ H", "age": 28, "sex": "Nam", "job": "Sinh viên", "specialty": "NỘI TIẾT",
            "reason": "Lơ mơ, thở nhanh sâu",
            "history": "- Viêm họng tự ý ngưng chích Insulin 3 ngày. Người lờ đờ, nói nhảm.",
            "past_medical": "- ĐTĐ type 1 từ năm 15 tuổi.",
            "clinical": "**Sinh hiệu:** HA 90/60 mmHg, Mạch 120 l/p, Thở Kussmaul 30 l/p.\n**Lâm sàng:** GCS 12, da khô héo, mùi hơi thở táo thối (Aceton).",
            "subclinical": "- **Đường mao mạch:** 28 mmol/L.\n- **Khí máu:** pH 7.08 (Toan máu), HCO3 6.\n- **Ketone máu:** 6.2 mmol/L. K+ 5.8.",
            "question": "👉 Xử trí Nhiễm toan Ceton (DKA) do ĐTĐ type 1. Cơ chế truyền dịch, cân bằng điện giải và pha tiêm Insulin?"
        },
        {
            "name": "Nguyễn Tú A", "age": 38, "sex": "Nữ", "job": "Kế toán", "specialty": "NỘI TIẾT",
            "reason": "Sụt cân 8kg, tim đập nhanh, run tay",
            "history": "- Ăn rất khoẻ nhưng sụt 8kg trong 3 tháng. Hồi hộp, mồ hôi đầm đìa, đi lỏng.",
            "past_medical": "- Rối loạn kinh nguyệt 6 tháng.",
            "clinical": "**Sinh hiệu:** Mạch nghỉ 105 l/p, HA 145/60.\n**Lâm sàng:** Run đầu chi (+), mắt lồi nhẹ, bướu cổ to độ II có rung miu.",
            "subclinical": "- **Hormone:** TSH < 0.01 mIU/L, FT4 52 pmol/L (Rất cao).\n- **Kháng thể:** TRAb 15 IU/L (+).",
            "question": "👉 Khẳng định Basedow (Cường giáp). Thuốc kháng giáp đường uống và thuốc chẹn beta phù hợp cho bệnh nhân?"
        },
        {
            "name": "Trần Thanh N", "age": 52, "sex": "Nữ", "job": "Công chức", "specialty": "NỘI TIẾT",
            "reason": "Tê rần bàn chân, tiểu đêm nhiều",
            "history": "- ĐTĐ 8 năm, dùng theo toa cũ. Dạo này chân như châm kim ban đêm, tiểu 4 lần/đêm.",
            "past_medical": "- ĐTĐ Type 2 đang uống Gliclazide 60mg. Suy thận mạn giai đoạn 3a.",
            "clinical": "**Sinh hiệu:** HA 145/90 mmHg.\n**Lâm sàng:** Mất cảm giác monofilament ngón 1 chân phải (Bệnh thần kinh ngoại biên).",
            "subclinical": "- **Thận:** Creatinin 1.3 mg/dL, eGFR 52, MAU 180 mg/g.\n- **HbA1c:** 8.5% (Tệ).",
            "question": "👉 Kế hoạch điều chỉnh thuốc ĐTĐ do tiến triển Biến chứng thận và Thần kinh đái tháo đường?"
        },
        {
            "name": "Đinh Công U", "age": 60, "sex": "Nam", "job": "Hưu trí", "specialty": "NỘI TIẾT",
            "reason": "Thường xuyên hạ đường huyết ban đêm",
            "history": "- Đang dùng Insulin liều trộn Mixtard 30. Hay vã mồ hôi ròng ròng lúc 3h sáng.",
            "past_medical": "- ĐTĐ 12 năm. HA ổn.",
            "clinical": "**Lâm sàng:** Không có dấu hiệu đặc biệt, thể trạng trung bình.",
            "subclinical": "- **Đường huyết mao mạch 3h sáng:** 2.8 - 3.1 mmol/L.\n- **Đường sáng lúc ngủ dậy:** 8 - 12 mmol/L (Hiệu ứng Somogyi).",
            "question": "👉 Phân biệt hiệu ứng Somogyi và hiện tượng Bình minh. Hướng chuyển đổi phác đồ Insulin nền mượt hơn?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 4: TIM MẠCH + HÔ HẤP (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫀+🫁 Tim + Hô hấp": [
        {
            "name": "Đỗ Trọng G", "age": 68, "sex": "Nam", "job": "Nông dân", "specialty": "TIM - HÔ HẤP",
            "reason": "Khó thở dữ dội, khạc đờm bọt hồng",
            "history": "- Đột ngột tỉnh khó thở chẹn ngực lúc nửa đêm, ho ra đờm bọt màu hồng nhạt.",
            "past_medical": "- COPD (GOLD D, FEV1 40%). Suy tim mạn (HFrEF 40%).",
            "clinical": "**Sinh hiệu:** HA 170/100, Mạch 115, SpO2 85%.\n**Lâm sàng:** Hoảng loạn. Phổi cực nhiều ran ẩm dâng lên đáy phổi (như sóng triều), TM cổ nổi.",
            "subclinical": "- **NT-proBNP:** 6500 pg/mL.\n- **Khí máu:** PaO2 55, pH 7.35.\n- **X-Quang:** Phù phổi cấp gốc.",
            "question": "👉 Cấp cứu Phù phổi cấp do suy tim trên bệnh nhân có kèm COPD. Liều thuốc lợi tiểu quai và Nitroglycerin?"
        },
        {
            "name": "Nguyên Khang V", "age": 66, "sex": "Nam", "job": "Bảo vệ", "specialty": "TIM - HÔ HẤP",
            "reason": "Đau ngực sau lưng kèm khó thở",
            "history": "- Đau ngực trái lan sau lưng 2 giờ nay ngột ngạt.",
            "past_medical": "- Hút thuốc lá 40 năm (COPD nhóm C). Tăng HA.",
            "clinical": "**Sinh hiệu:** HA 180/110, Mạch 100 l/p, SpO2 88%.\n**Lâm sàng:** Phổi rít, Tím môi nhẹ.",
            "subclinical": "- **ECG:** ST chênh V4-V6.\n- **Troponin T:** 89 ng/L.\n- **D-dimer:** 800 ng/mL.",
            "question": "👉 Chẩn đoán phân biệt NMCT cấp NSTEMI hay Nhồi máu phổi đồng phát (do D-Dimer tăng nhẹ)? Chỉ định xét nghiệm?"
        },
        {
            "name": "Lê Phước S", "age": 74, "sex": "Nam", "job": "Hưu", "specialty": "TIM - HÔ HẤP",
            "reason": "Ho khan kéo dài, phù nhẹ mắt cá",
            "history": "- Khó thở tăng 2 tuần, đôi khi ho khan nửa đêm.",
            "past_medical": "- Rung nhĩ vĩnh viễn (Rivaroxaban 15mg), HFpEF (EF 58%).\n- COPD nhóm B.",
            "clinical": "**Sinh hiệu:** HA 155/90, SpO2 91%.\n**Lâm sàng:** Tim loạn nhịp, Ran ẩm đáy phổi nhẹ, phù mắt cá.",
            "subclinical": "- **Hô hấp ký:** Gần nhất FEV1 55%.\n- **BNP:** 450 pg/mL.\n- **X-Quang:** Tái phân bố tuần hoàn.",
            "question": "👉 Tính chất của đợt cấp COPD và đợt suy tim cấp khá tương đồng, tiêu điểm để phân biệt qua BN và Siêu âm là gì?"
        },
        {
            "name": "Nguyễn Ngọc B", "age": 60, "sex": "Nữ", "job": "Thợ may", "specialty": "TIM - HÔ HẤP",
            "reason": "Ho thành tràng liên tục 1 tháng, ngứa họng",
            "history": "- Không sốt, ho khan khan ngứa họng. Khó thở mức nền.",
            "past_medical": "- Vừa bị NMCT thành trước 5 năm. Suy tim HFrEF.\n- Đang uống ACE inhibitors (Enalapril), Spirnolactone, Tiotropium xịt.",
            "clinical": "**Lâm sàng:** Phổi rất trong, không khò khè. Tim đều.",
            "subclinical": "- **X-quang:** Không tổn thương mới.\n- **BNP:** 280 pg/mL (ổn định).",
            "question": "👉 Tác dụng phụ ho khan do nhóm ức chế men chuyển ảnh hưởng nhầm quy cho COPD? Hướng đổi ARBs?"
        },
        {
            "name": "Võ Hoàng L", "age": 78, "sex": "Nam", "job": "Buôn bán nhỏ", "specialty": "TIM - HÔ HẤP",
            "reason": "Ngất thoáng qua tại toilet, mệt mỏi",
            "history": "- Sáng đi tiêu rặn ngất khoảng 2 phút. Khó thở mạn tính tăng lên.",
            "past_medical": "- Rung nhĩ (đang dùng Digoxin 0.25). COPD nặng. CABG 8 năm.",
            "clinical": "**Sinh hiệu:** Mạch chậm 50 l/p (loạn nhịp hoàn toàn), HA 105/65.\n**Lâm sàng:** Tĩnh mạch cổ nổi, phù.",
            "subclinical": "- **Digoxin:** 3.2 ng/mL (Ngộ độc độc tính).\n- **Kali máu:** 5.8 mEq/L (Cao).",
            "question": "👉 Ngộ độc Digoxin gây nhịp chậm gây ngất làm tồi tệ suy hô hấp/suy tim. Thái độ giải độc và ngừng ngay Digoxin?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 5: TIM MẠCH + NỘI TIẾT (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫀+🔬 Tim + Nội tiết": [
        {
            "name": "Mai Thanh C", "age": 63, "sex": "Nam", "job": "Kinh doanh", "specialty": "TIM MẠCH - NỘI TIẾT",
            "reason": "Đau ngực thắt khi leo dốc",
            "history": "- 2 tuần nay, mỗi buổi đi dốc độ 100m là đau thắt ngực (CCS II). Nghỉ 5 phút tự dịu.",
            "past_medical": "- ĐTĐ type 2 (10 năm mất kiểm soát).\n- Tăng HA.",
            "clinical": "**Sinh hiệu:** HA 150/95 mmHg.\n**Lâm sàng:** Tim đều, nhịp không tiếng ngựa phi.",
            "subclinical": "- **HbA1c:** 8.8%. FPG 11.2.\n- **Thận:** Creatinin 1.6 mg/dL (eGFR 42).\n- **ECG:** (+) Nghiệm pháp gắng sức.",
            "question": "👉 Bệnh nhân suy thận độ 3 và Bệnh cơ tim do ĐTĐ. Có nên chỉ định ưu tiên SGLT2i để bảo vệ kép cho cả tim/thận?"
        },
        {
            "name": "Lưu Văn Đ", "age": 50, "sex": "Nam", "job": "Kỹ sư", "specialty": "TIM MẠCH - NỘI TIẾT",
            "reason": "Huyết áp rất cao, liệt chi yếu cơ",
            "history": "- Đo HA luôn 165/100 mmHg dù tự ý uống tới 3 loại thuốc. Chân cẳng bủn rủn, mỏi rã.",
            "past_medical": "- Tăng HA kháng trị.",
            "clinical": "**Sinh hiệu:** HA 168/102.\n**Lâm sàng:** Trương lực cơ yếu, không dấu thần kinh khu trú.",
            "subclinical": "- **Khoáng:** K+ máu sụt (2.8 mEq/L).\n- **Renin/Aldosterone:** Tỷ lệ ARR = 45 (Rất cao).\n- **CT Bụng:** U tuyến thượng thận trái 15mm.",
            "question": "👉 Hội chứng Conn (U tủy thượng thận cường Aldosterone). Cắt khối u nội soi và thuốc đặc hiệu Spironolactone trước mổ?"
        },
        {
            "name": "Bạch Thủy M", "age": 55, "sex": "Nữ", "job": "Tạo mẫu", "specialty": "TIM MẠCH - NỘI TIẾT",
            "reason": "Tiểu nhiều, sụt cân, khám phát hiện rắc rối tim",
            "history": "- Khát nước sụt 3kg/tháng. Ăn ngọt nhiều hơn.",
            "past_medical": "- HA cao uống Amlodipin lâu.",
            "clinical": "**Lâm sàng:** Tim ngựa phi T3. Gan tĩnh mạch cổ nổi.",
            "subclinical": "- **Đường:** HbA1c 7.2%. Lipid cao.\n- **Siêu âm:** LVEF 45%, E/e' = 14.\n- **Nước tiểu:** MicroAlbumin đi theo 120 mg/g.",
            "question": "👉 Chẩn đoán Suy tim phân suất tống máu giảm nhẹ trên ca ĐTĐ mới kiểm soát. Phác đồ nội khoa ưu tiên Quadruple Therapy?"
        },
        {
            "name": "Vũ Anh K", "age": 45, "sex": "Nữ", "job": "Hướng dẫn viên", "specialty": "TIM MẠCH - NỘI TIẾT",
            "reason": "Ngất, cấp cứu sau đánh trống ngực",
            "history": "- Bị rung thất và được sốc điện trên đường vào. Đang kích thích vật vã dữ dội.",
            "past_medical": "- Cường giáp Basedow (Tự ý bỏ thuốc 2 tuần nay).",
            "clinical": "**Sinh hiệu:** Rung nhĩ đáp ứng rất nhanh (140 l/p), HA 160/60, Sốt 38.8.\n**Lâm sàng:** Lồi mắt, tuyến giáp to.",
            "subclinical": "- **Keystones:** FT4=85 (Rất ấn tượng); TSH<0.01.\n- **Men tim:** Troponin 45 ng/L.",
            "question": "👉 Cơn bão Giáp trạng (Thyroid storm) gây chèn ép lên điện sinh tim mạch. Sử dụng Beta-blocker nhanh qua đường tĩnh mạch và kháng giáp?"
        },
        {
            "name": "Hà Diệu L", "age": 70, "sex": "Nữ", "job": "Hưu trí", "specialty": "TIM MẠCH - NỘI TIẾT",
            "reason": "Khó thở lên NYHA III, cân nặng phù rụt",
            "history": "- Tăng 3kg trong 2 tuần gần nhất. Tối không nằm thở được.",
            "past_medical": "- Suy tim HFpEF (EF 55%). ĐTĐ type 2 BMI 35.",
            "clinical": "**Sinh hiệu:** Phù 2 chân to.\n**Lâm sàng:** Chán ăn.",
            "subclinical": "- **Thận:** Creatinin 1.4 mg/dL. NT-proBNP 1800.",
            "question": "👉 Sự tiến hóa thành đợt mất bù cấp trên nền HFpEF và Đái tháo đường. Lợi tiểu Furosemide tĩnh mạch + Xem xét tăng Metformin?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 6: HÔ HẤP + NỘI TIẾT (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫁+🔬 Hô hấp + Nội tiết": [
        {
            "name": "Đào Thị O", "age": 58, "sex": "Nữ", "job": "Buôn bán", "specialty": "HÔ HẤP - NỘI TIẾT",
            "reason": "Ho đờm dai dẳng, đường huyết tăng vọt",
            "history": "- Mua Prednisolone uống liên miên trị Hen mỗi bị khi khò khè. Dạo nay thèm ngọt mệt lả.",
            "past_medical": "- ĐTĐ type 2 (12 năm). Béo phì cục bộ.",
            "clinical": "**Lâm sàng:** Xương giòn, hình thể Cushing (mặt trăng đầy đặn).",
            "subclinical": "- **HbA1c:** 9.2% (Tăng vọt quá cao).\n- **Đo mật độ:** DEXA Cột sống -2.1.",
            "question": "👉 Sự phá huỷ kiểm soát đường huyết do dùng Corticoid trị Hen bừa bãi. Quyết sách nâng phác đồ ICS và loại bỏ Corticoid miệng?"
        },
        {
            "name": "Lương Hữu V", "age": 70, "sex": "Nam", "job": "Trồng trọt", "specialty": "HÔ HẤP - NỘI TIẾT",
            "reason": "Sụt cân suy kiệt, choáng liên tục do hạ đường",
            "history": "- Thường xuyên ngất hạ đường (3.0 mmol/L) ban ngày. Teo cơ vô lực.",
            "past_medical": "- COPD nặng thở oxy nhà, ĐTĐ 2.",
            "clinical": "**Sinh hiệu:** HA 90/60.\n**Lâm sàng:** Hội chứng suy kiệt hô hấp.",
            "subclinical": "- **Cortisol:** 2.5 μg/dL (Quá ức chế hệ thượng thận).\n- **ACTH:** 85.",
            "question": "👉 Suy vỏ thượng thận tự phát. Sự nguy hiểm của sốc suy tuyến do dùng nhầm Corticoid thời gian dài qua đường họng trị COPD."
        },
        {
            "name": "Đỗ Quang V", "age": 62, "sex": "Nam", "job": "Thợ thủ công", "specialty": "HÔ HẤP - NỘI TIẾT",
            "reason": "Tìm ra cả đường huyết cao sau khám tình cờ",
            "history": "- Tình cờ xét nghiệm tiểu đường 8.5 mmo/L.",
            "past_medical": "- Bỏ thuốc lá một năm. Có hội chứng nghẽn nhịp thở.",
            "clinical": "**Lâm sàng:** Vòng eo 102cm mập mạp.",
            "subclinical": "- **Hô hấp ký:** Tắc nghẽn nhẹ (0.65).\n- **X Quang:** Ứ khí.",
            "question": "👉 Chẩn đoán mới Hội chứng Chuyển hóa kẹp cả Rối loạn Mỡ máu. Tư vấn dùng GLP-1 giảm cân cho bệnh nhân COPD?"
        },
        {
            "name": "Trần Thanh B", "age": 65, "sex": "Nữ", "job": "Đầu bếp", "specialty": "HÔ HẤP - NỘI TIẾT",
            "reason": "Khó thở bất thình lình, sụt cân",
            "history": "- Dù đang dùng hít COPD hằng ngày, nhưng 1 tháng qua ốm o 4 kg, tức thở kinh hồn.",
            "past_medical": "- Basedow, COPD nhẹ.",
            "clinical": "**Sinh hiệu:** Mạch nhanh 110 l/p, HA 150/60.\n**Lâm sàng:** Phổi rít nhẹ.",
            "subclinical": "- **Tuyến giáp:** TSH < 0.05. FT4 cao ngút.\n- **ECG:** AFib 120/p.",
            "question": "👉 Giọt nước tràn ly (Cơn bão cường giáp). Việc tăng nhịp do Basedow khiến dung tích phổi xẹp. Kiểm soát nhịp tim khẩn."
        },
        {
            "name": "Nguyên Tuấn Q", "age": 55, "sex": "Nam", "job": "Bác sĩ thú y", "specialty": "HÔ HẤP - NỘI TIẾT",
            "reason": "Tăng tiết vi khuẩn phổi",
            "history": "- Đợt cấp COPD với đờm đục từ 3 ngày qua. Nhập viện thở máy.",
            "past_medical": "- ĐTĐ type 2. Đang dùng Corticoid.",
            "clinical": "**Sinh hiệu:** Sốt 38.2, 88% SpO2.",
            "subclinical": "- **Đường huyết:** Tăng điên cuồng 18-25 mmol/L (Dù vẫn cho uống Empagliflozin).",
            "question": "👉 Đợt viêm cấp kích hoạt tình trạng kháng cực Insulin. Hướng dẫn chuyển sang xài Insulin tĩnh mạch ngắt nghỉ trong đợt hồi sức."
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 7: CẢ 3 KHOA (TIM MẠCH + HÔ HẤP + NỘI TIẾT) (5 CA)
    # ──────────────────────────────────────────────────────────
    "🫀🫁🔬 Cả 3 khoa": [
        {
            "name": "Châu Trí P", "age": 72, "sex": "Nam", "job": "Hưu trí", "specialty": "ĐA KHOA CẤP CỨU",
            "reason": "Hôn mê, suy hô hấp nặng bọt hồng",
            "history": "- Ngày hôm trước khạc bọt hồng bồn chồn. Nay thì mê man, gọi không tỉnh.",
            "past_medical": "- ĐTĐ type 2 (HbA1c 8.5%).\n- Suy tim HFrEF (LVEF 30%).\n- COPD nhóm C.",
            "clinical": "**Sinh hiệu:** HA 160/90 mmHg, SpO2 84%.",
            "subclinical": "- **Đường máu:** 22.0 mmol/L.\n- **Khí máu:** Toan nặng PaCO2 55.\n- **X-Quang:** Phù phổi cấp trắng xoá.",
            "question": "👉 Cú đấm đa bệnh lý phối hợp (Hôn mê nội tiết + Suy thở CO2 + O2 máu tồi). Bóp bóng thở máy và Loop Diuretics ưu tiên?"
        },
        {
            "name": "Ngô Bách T", "age": 58, "sex": "Nam", "job": "Giám đốc", "specialty": "ĐA KHOA",
            "reason": "Đau đầu chém, huyết áp chọc trời nhói ngực",
            "history": "- Nửa đêm ngáy lịm ngưng thở, vợ hốt hoảng.",
            "past_medical": "- ĐTĐ 2 mất quản lý, OSA (tắt nghẽn đường thở).",
            "clinical": "**Sinh hiệu:** HA 220/130 mmHg cực kỳ lớn.\n**Lâm sàng:** Béo BMI 36.",
            "subclinical": "- **Ngáy ngủ:** AHI 42.\n- **Siêu âm:** Phì đại ĐMP cấp.",
            "question": "👉 Cơn bão Tăng áp phổi và Ngộ độc HA cực lớn tác động xói mòn tim não. Lệnh thở máy CPAP kết hợp Nitroglycerin truyền tốc độ."
        },
        {
            "name": "Lương Lữ H", "age": 68, "sex": "Nữ", "job": "Nội trợ", "specialty": "ĐA KHOA TỔNG HỢP",
            "reason": "Mạch chậm lỳ, phù tấy hai cổ chân nặng chân",
            "history": "- Đi nhẹ nhàng khoảng 1 tầng đã mệt. Chân nặng như cùm.",
            "past_medical": "- Tắc ngẽn đặt 2 stent.\n- COPD nhóm B.\n- ĐTĐ ổn.",
            "clinical": "**Sinh hiệu:** Mạch 62/p cực chậm nhạt.\n**Lâm sàng:** Bóng tim tăng, mệt do nghẽn tĩnh mạch sâu.",
            "subclinical": "- **Siêu âm:** LVEF giảm cực mạnh còn 42%.\n- **Thận:** eGFR 48.",
            "question": "👉 Tiến triển suy tim im lặng sau Đặt Stent kết hợp. Nhóm thuốc nào ARNI đang làm gánh nặng Thận quá tải?"
        },
        {
            "name": "Phan Hữu Q", "age": 75, "sex": "Nam", "job": "Về hưu", "specialty": "ICU ĐA KHOA",
            "reason": "Điều trị máy ngày 5, thông số nhiễm trùng tồi tệ",
            "history": "- Nằm thở ICU xâm lấn. Nay tụt huyết áp sốc vô vọng.",
            "past_medical": "- NMCT cũ (35%), Đáng xài Insulin cho Tiểu đường, COPD mạn.",
            "clinical": "**Sinh hiệu:** HA 90/55 lơ lửng dù chích Nor-epi.",
            "subclinical": "- **Creatinin:** Phá hủy thận lên 2.8.\n- **Lactate:** 4.8. Cấy khuẩn viêm nhiễm (Procalcitonin 8.5).",
            "question": "👉 Sốc nhiễm trùng đa tạng phổi (Viêm phổi do thở máy VAP). Phác đồ kháng sinh phổ rộng theo kháng sinh đồ khoa hồi sức?"
        },
        {
            "name": "Hoàng Tuyết O", "age": 64, "sex": "Nữ", "job": "Kế toán", "specialty": "NỘI ĐA KHOA NẶNG",
            "reason": "Phù to toàn thân trăng mọng",
            "history": "- Da ướt sũng. Bệnh nhân khó thở NYHA IV ráng sức ngáp ngáp.",
            "past_medical": "- Mắc COPD nhóm D, eGFR thảm hại dưới 22, HF.",
            "clinical": "**Sinh hiệu:** HA 100/60.\n**Lâm sàng:** Ran ẩm bung lụa 2 bên ốp phổi.",
            "subclinical": "- **Thận:** Lợi Kali quá tải (6.2). Na thấp.\n- **Hb:** Dưới 8.5 g/dL gây xỉu.",
            "question": "👉 Suy đa cơ quan tận cùng (Suy tim + Suy gan thận cấp). Có chỉ định lọc máu liên tục CRT cho đối tượng rủi ro tuổi?"
        }
    ],
}

# ── Danh sách nhóm theo thứ tự hiển thị ─────────────────────
CATEGORY_ORDER_ROW1 = ["🫀 Tim mạch", "🫁 Hô hấp", "🔬 Nội tiết"]
CATEGORY_ORDER_ROW2 = ["🫀+🫁 Tim + Hô hấp", "🫀+🔬 Tim + Nội tiết", "🫁+🔬 Hô hấp + Nội tiết", "🫀🫁🔬 Cả 3 khoa"]

def get_random_case(category: str) -> dict:
    """
    Chọn ngẫu nhiên 1 ca bệnh từ nhóm chuyên khoa và tự động cấu trúc hóa
    nội dung ca bệnh thành Bệnh án Nội khoa.
    """
    cases = SAMPLE_CASE_BANK.get(category, [])
    if not cases:
        return {"text": "", "age": 0, "sex": "Nam", "specialty": "Tự động nhận diện"}
    
    selected_case = random.choice(cases)
    
    # Định dạng lại văn bản
    formatted_text = format_case(selected_case)
    
    # Trả về dict mới chứa text đã định dạng để app.py dùng
    return {
        "text": formatted_text,
        "age": selected_case["age"],
        "sex": selected_case["sex"],
        "specialty": selected_case["specialty"]
    }
