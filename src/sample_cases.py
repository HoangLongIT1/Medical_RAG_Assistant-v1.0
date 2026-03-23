"""
sample_cases.py – Ngân hàng ca bệnh mẫu ngẫu nhiên
Được định dạng chuẩn theo cấu trúc Bệnh án Nội khoa Lâm sàng.
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
# NGÂN HÀNG CA BỆNH MẪU CẤU TRÚC — 7 NHÓM
# ══════════════════════════════════════════════════════════════

SAMPLE_CASE_BANK = {

    # ──────────────────────────────────────────────────────────
    # NHÓM 1: TIM MẠCH
    # ──────────────────────────────────────────────────────────
    "🫀 Tim mạch": [
        {
            "name": "Trần Văn M", "age": 70, "sex": "Nam", "job": "Hưu trí", "specialty": "TIM MẠCH",
            "reason": "Nhịp tim rất chậm, khó thở khi nằm",
            "history": "- Bệnh nhân mệt mỏi nhiều 2 ngày nay.\n- Sáng nay đột ngột thấy choáng váng, khó thở nhiều khi nằm, phải kê cao gối hoặc ngồi thở.\n- Chưa dùng thuốc gì thêm tại nhà.",
            "past_medical": "- Suy tim HFrEF (EF 35%) đang điều trị nội khoa.\n- Đang dùng: Bisoprolol 5mg/ngày, Enalapril 5mg/ngày.",
            "clinical": "**Toàn thân:** Tỉnh, tiếp xúc được. Tay chân lạnh ẩm.\n**Sinh hiệu:** HA 85/50 mmHg, Mạch 40 lần/phút, SpO2 92%.\n**Tim mạch:** Nhịp chậm đều, không âm thổi.\n**Hô hấp:** Thở co kéo nhẹ, ran ẩm 2 đáy phổi.",
            "subclinical": "- **ECG:** Block nhĩ thất độ III.\n- **NT-proBNP:** 5800 pg/mL (tăng rất cao).\n- **Siêu âm tim:** Giảm động đa vùng, LVEF 30%.",
            "question": "👉 Có nên tiếp tục hoặc tăng liều thuốc chẹn beta (Bisoprolol) cho bệnh nhân trong bối cảnh huyết động không ổn định này không? Hướng xử trí cấp cứu tiếp theo?"
        },
        {
            "name": "Lê Thị H", "age": 62, "sex": "Nữ", "job": "Nội trợ", "specialty": "TIM MẠCH",
            "reason": "Đau ngực trái dữ dội",
            "history": "- Cách nhập viện 45 phút, bệnh nhân đột ngột đau thắt ngực trái dữ dội lan lên hàm và vai trái.\n- Kèm vã mồ hôi hột, buồn nôn, cảm giác hoảng sợ.",
            "past_medical": "- Tăng huyết áp 10 năm (Amlodipin 10mg, Losartan 50mg).\n- Dị ứng: Aspirin (gây phù mạch, mề đay).",
            "clinical": "**Toàn thân:** Vã mồ hôi nhiều, da niêm nhạt.\n**Sinh hiệu:** HA 160/95 mmHg, Mạch 95 lần/phút, SpO2 96%.\n**Tim mạch:** Nhịp tim đều, T1 T2 rõ, không tiếng ngựa phi.",
            "subclinical": "- **ECG:** ST chênh lên ở DII, DIII, aVF (Nhồi máu cơ tim thành dưới).\n- **Troponin T hs:** 250 ng/L (bình thường < 14 ng/L).",
            "question": "👉 Chẩn đoán Nhồi máu cơ tim cấp (STEMI) thành dưới. Bệnh nhân có tiền sử dị ứng Aspirin nặng, cần sử dụng phác đồ kháng kết tập tiểu cầu nào thay thế để chuẩn bị can thiệp PCI?"
        },
        {
            "name": "Hoàng Văn K", "age": 55, "sex": "Nam", "job": "Nhân viên văn phòng", "specialty": "TIM MẠCH",
            "reason": "Đánh trống ngực, hồi hộp từng cơn",
            "history": "- Xuất hiện cơn hồi hộp 3 tháng nay, rải rác 1-2 lần/tuần, kéo dài 30 phút - vài giờ rồi tự hết.\n- Khi lên cơn thấy chóng mặt nhẹ, không ngất.",
            "past_medical": "- Tăng huyết áp 5 năm, quản lý khá tốt bằng Enalapril 10mg.",
            "clinical": "**Toàn thân:** Khỏe, tỉnh táo.\n**Sinh hiệu:** HA 140/85 mmHg, Mạch 82 lần/phút (không đều).\n**Tim phổi:** Loạn nhịp hoàn toàn, T1 rõ.",
            "subclinical": "- **ECG:** Rung nhĩ đáp ứng thất trung bình.\n- **Siêu âm tim:** Nhĩ trái giãn 42mm, EF 55%, không thấy huyết khối tiểu nhĩ.",
            "question": "👉 Tính điểm CHA2DS2-VASc cho bệnh nhân này? Quyết định bắt đầu sử dụng thuốc kháng đông (NOACs hay kháng vitamin K) dựa trên phác đồ hiện tại ra sao?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 2: HÔ HẤP
    # ──────────────────────────────────────────────────────────
    "🫁 Hô hấp": [
        {
            "name": "Phạm Văn T", "age": 58, "sex": "Nam", "job": "Công nhân", "specialty": "HÔ HẤP",
            "reason": "Khó thở dữ dội, ho khạc đờm mủ xanh",
            "history": "- Ho tăng dần 3 ngày nay, đờm chuyển từ trắng sang vàng xanh.\n- Kèm sốt 38.5 độ C, khó thở liên tục phải ngồi dậy để thở.",
            "past_medical": "- COPD 8 năm (FEV1 38%), đang dùng Tiotropium và Budesonide/Formoterol.\n- Thường xuyên có các đợt cấp (2 lần trong năm ngoái).",
            "clinical": "**Toàn thân:** Mệt mỏi, vã mồ hôi, tím môi nhẹ.\n**Sinh hiệu:** HA 130/80 mmHg, Mạch 105 lần/phút, Nhịp thở 28 lần/phút, SpO2 86% (khí trời).\n**Hô hấp:** Co kéo cơ hô hấp phụ, phổi nghe ran rít, ran ngáy và ran nổ 2 đáy.",
            "subclinical": "- **Khí máu động mạch:** pH 7.32, PaCO2 58 mmHg, PaO2 52 mmHg, HCO3 28 mEq/L.\n- **X-quang ngực:** Phổi ứ khí nhiều, thâm nhiễm đáy phổi trái.",
            "question": "👉 Bệnh nhân đang trải qua Đợt cấp COPD mức độ nặng (Toan hô hấp). Liệt kê trình tự xử trí cấp cứu hô hấp (thở máy NIV, kháng sinh, corticoid, giãn phế quản) chuẩn phác đồ Bộ Y Tế?"
        },
        {
            "name": "Nguyễn Thị L", "age": 45, "sex": "Nữ", "job": "Giáo viên", "specialty": "HÔ HẤP",
            "reason": "Ho khan kéo dài, khò khè về đêm",
            "history": "- Ho kéo dài hơn 6 tuần, ho khan, nặng lên vào rạng sáng hoặc khi gặp gió lạnh.\n- Có những lúc cảm thấy nặng ngực và phát ra tiếng rít khò khè.",
            "past_medical": "- Viêm mũi dị ứng mạn tính.\n- Không hút thuốc lá.",
            "clinical": "**Sinh hiệu:** HA 120/70 mmHg, Mạch 80 lần/phút, SpO2 98%.\n**Hô hấp:** Phổi rì rào phế nang êm, gõ trong, nghe thấy rải rác ran rít nhỏ cuối thì thở ra.",
            "subclinical": "- **Hô hấp ký:** FEV1 82%, Test phục hồi phế quản (+): FEV1 tăng 15% và 250ml sau Salbutamol.\n- **FeNO:** 45 ppb (Viêm đường thở dị ứng).",
            "question": "👉 Chẩn đoán Hen phế quản ở người lớn. Khuyến cáo bậc điều trị ban đầu (GINA hoặc Bộ Y Tế) cho trường hợp với tần suất triệu chứng như trên là gì?"
        },
        {
            "name": "Trần Thị D", "age": 72, "sex": "Nữ", "job": "Hưu trí", "specialty": "HÔ HẤP",
            "reason": "Khó thở kịch phát, đau nhói ngực phải",
            "history": "- Sáng nay đột nhiên khó thở dữ dội, kèm cơn đau nhói ở ngực bên phải nhất là khi hít sâu.",
            "past_medical": "- Vừa phẫu thuật thay khớp háng phải cách đây 10 ngày, bất động tại giường phần lớn thời gian.\n- BMI 32.",
            "clinical": "**Toàn thân:** Thể trạng béo, vã mồ hôi.\n**Sinh hiệu:** HA 100/70 mmHg, Mạch 110 lần/phút, Nhịp thở 26 lần/phút, SpO2 90%.\n**Chân phải:** Sưng nề to hơn chân trái, ấn đau nhẹ vùng bắp chân.",
            "subclinical": "- **D-dimer:** > 5000 ng/mL.\n- **ECG:** Nhịp nhanh xoang, dạng S1Q3T3 trên điện tâm đồ.\n- **Khí máu:** PaO2 62 mmHg, PaCO2 30 mmHg (Kiềm hô hấp).",
            "question": "👉 Bệnh nhân có nguy cơ rất cao Thuyên tắc phổi (Pulmonary Embolism). Điểm Wells lâm sàng của ca này? Chỉ định hình ảnh học nào tiếp theo để chẩn đoán xác định và phác đồ thuốc chống đông?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 3: NỘI TIẾT
    # ──────────────────────────────────────────────────────────
    "🔬 Nội tiết": [
        {
            "name": "Bùi Văn P", "age": 45, "sex": "Nam", "job": "Quản lý kinh doanh", "specialty": "NỘI TIẾT",
            "reason": "Phát hiện đường huyết cao khi khám sức khỏe",
            "history": "- Không có triệu chứng ăn nhiều, uống nhiều, tiểu nhiều hay sụt cân.\n- Xét nghiệm máu định kỳ tuần trước báo đường cao.",
            "past_medical": "- Bố bị ĐTĐ type 2 năm 50 tuổi.\n- Thừa cân (BMI 27.5).",
            "clinical": "**Sinh hiệu:** HA 135/85 mmHg.\n**Toàn thân:** Béo bụng, vòng eo 96cm. Không có dấu gai đen.",
            "subclinical": "- **Đường huyết đói (FPG):** Lần 1: 7.5 mmol/L. Lần 2 (hôm nay): 7.8 mmol/L.\n- **HbA1c:** 6.8%.\n- **Lipid:** Cholesterol 5.8 mmol/L, LDL 3.5 mmol/L.",
            "question": "👉 Tiêu chuẩn chẩn đoán chuẩn xác cho thấy bệnh nhân đã mắc ĐTĐ type 2. Lựa chọn thuốc đầu tay khởi trị và mục tiêu HbA1c kỳ vọng cần đạt là bao nhiêu?"
        },
        {
            "name": "Lê Vũ H", "age": 28, "sex": "Nam", "job": "Sinh viên", "specialty": "NỘI TIẾT",
            "reason": "Lơ mơ, khó thở nhanh sâu",
            "history": "- 3 ngày trước bị viêm họng, sốt cao, tự ý bỏ tiêm Insulin vì không ăn uống được.\n- Tối nay người nhà thấy lơ mơ, gọi hỏi trả lời chậm nên đưa vào cấp cứu.",
            "past_medical": "- ĐTĐ type 1 từ năm 15 tuổi (phác đồ Glargine + Novorapid).",
            "clinical": "**Toàn thân:** Lơ mơ (GCS 12), da phản khô, độ đàn hồi da (turgor) giảm nghiêm trọng, hơi thở có mùi trái cây thối (Aceton).\n**Sinh hiệu:** HA 90/60 mmHg, Mạch 120 lần/phút, Nhịp thở 30 lần/phút (thở Kussmaul).",
            "subclinical": "- **Đường mao mạch:** 28 mmol/L (rất cao).\n- **Khí máu:** pH 7.08 (toan máu nặng), HCO3 6 mEq/L.\n- **Ketone máu:** 6.2 mmol/L.\n- **Điện giải:** K+ 5.8 mEq/L.",
            "question": "👉 Chẩn đoán Toan Ceton do ĐTĐ (DKA). Phác đồ bù dịch (mức độ ưu tiên cao nhất), kiểm soát hạ Kali máu và sử dụng Insulin tĩnh mạch liên tục được quy định như thế nào?"
        },
        {
            "name": "Nguyễn Tú A", "age": 38, "sex": "Nữ", "job": "Kế toán", "specialty": "NỘI TIẾT",
            "reason": "Sụt cân nhanh, run tay, tim đập nhanh",
            "history": "- Bệnh nhân sụt hẳn 8kg trong 3 tháng qua dù ăn rất khoẻ.\n- Luôn cảm thấy nóng bức, đổ mồ hôi nhiều lúc làm việc, hay run tay khi cầm cốc nước uống, đi tiêu lỏng 3-4 lần/ngày.",
            "past_medical": "- Không ghi nhận tiền sử bệnh lý tự miễn. Rối loạn kinh nguyệt 6 tháng nay.",
            "clinical": "**Toàn thân:** Thể trạng gầy, run tĩnh đầu chi (+), ra mồ hôi tay.\n**Mắt:** Lồi mắt nhẹ 2 bên, có dấu hiệu co trợn mi.\n**Cổ:** Bướu giáp to độ II lan toả, mật độ mềm, rung miu (+).\n**Sinh hiệu:** Mạch 105 lần/phút, HA 145/60 mmHg.",
            "subclinical": "- **Hormone:** TSH < 0.01 mIU/L, FT4: 52 pmol/L (tăng cao).\n- **Kháng thể:** TRAb 15 IU/L (Dương tính mạnh).",
            "question": "👉 Chẩn đoán bệnh Basedow (Cường giáp). Trong đợt cấp điều trị, cần lựa chọn nhóm thuốc kháng giáp tổng hợp nào và thuốc ức chế triệu chứng giao cảm đi kèm?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 4: TIM MẠCH + HÔ HẤP
    # ──────────────────────────────────────────────────────────
    "🫀+🫁 Tim + Hô hấp": [
        {
            "name": "Đỗ Trọng G", "age": 68, "sex": "Nam", "job": "Nông dân", "specialty": "TIM MẠCH VÀ HÔ HẤP",
            "reason": "Khó thở dữ dội, khạc đờm bọt hồng",
            "history": "- Đột ngột tỉnh giấc lúc nửa đêm vì khó thở chẹn ngực, phải ngồi dậy ôm gối hít thở.\n- Ho khạc ra ít đờm có màu trắng lẫn chút bọt hồng.",
            "past_medical": "- COPD (GOLD D, FEV1 40%).\n- Suy tim mạn (HFrEF, EF 40%).\n- Đang dùng xịt thuốc Budesonide/Formoterol, uống Bisoprolol và Furosemide.",
            "clinical": "**Toàn thân:** Vật vã kích thích, vã mồ hôi hột.\n**Sinh hiệu:** HA 170/100 mmHg, Mạch 115 lần/phút, SpO2 85%.\n**Phổi:** Rất nhiều ran rít, ran ẩm dâng lên từ hai đáy phổi (như sóng triều).\n**Tim mạch:** Tĩnh mạch cổ nổi to.",
            "subclinical": "- **NT-proBNP:** 6500 pg/mL.\n- **Khí máu:** PaO2 55, PaCO2 48, pH 7.35.\n- **Siêu âm tim tại giường:** LVEF 35%, tăng áp lực tĩnh mạch trung tâm.",
            "question": "👉 Chẩn đoán Phù phổi cấp huyết động trên nền bệnh nhân COPD/Suy tim. Thuốc lợi tiểu quai đường tĩnh mạch và Nitroglycerin giãn mạch cần được chỉ định với liều lượng bao nhiêu?"
        },
        {
            "name": "Nguyên Khang V", "age": 66, "sex": "Nam", "job": "Bảo vệ", "specialty": "TIM MẠCH VÀ HÔ HẤP",
            "reason": "Đau ngực lan lưng kèm khó thở",
            "history": "- Đau ngực trái liên tục 2 giờ nay, cảm giác chèn ép, đau lan ra sau lưng.\n- Cảm thấy khó thở nhịp nhành, ngột ngạt.",
            "past_medical": "- Hút thuốc 40 gói-năm (COPD nhóm C).\n- Tăng huyết áp đang điều trị Amlodipin.",
            "clinical": "**Toàn thân:** Tím tái nhẹ đầu chi.\n**Sinh hiệu:** HA 180/110 mmHg, Mạch 100 lần/phút, SpO2 88%.\n**Phổi:** Thở ran rít 2 bên, có ran ẩm nhẹ ở rìa đáy phổi.",
            "subclinical": "- **ECG:** ST chênh xuống V4-V6, T âm sâu V1-V3.\n- **Troponin T hs:** 89 ng/L (tăng).\n- **D-dimer:** 800 ng/mL.",
            "question": "👉 Bệnh nhân có hình ảnh tổn thương thiếu máu cơ tim (NSTEMI) kèm D-dimer tăng trên nền COPD. Cần chỉ định khẩn cấp phương tiện ưu tiên nào (CT-Scan mạch máu phổi hay Chụp mạch vành) và vì sao?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 5: TIM MẠCH + NỘI TIẾT
    # ──────────────────────────────────────────────────────────
    "🫀+🔬 Tim + Nội tiết": [
        {
            "name": "Mai Thanh C", "age": 63, "sex": "Nam", "job": "Kinh doanh", "specialty": "TIM MẠCH VÀ NỘI TIẾT",
            "reason": "Đau ngực thắt khi đi bộ lên dốc",
            "history": "- 2 tuần nay, mỗi buổi tập thể dục đi bộ lên dốc cầu vượt khoảng 100m là bị đau thắt ngực (ccs II).\n- Nghỉ chân 5 phút thì cơn đau tự dịu.",
            "past_medical": "- ĐTĐ type 2 (10 năm), HA cao (8 năm), men gan cao.\n- Tự ý bỏ điều trị đái tháo đường 6 tháng.",
            "clinical": "**Sinh hiệu:** HA 150/95 mmHg, Mạch 88 lần/phút.\n**Tim mạch:** Nhịp đều, không tiếng bất thường.",
            "subclinical": "- **HbA1c:** 8.8%.\n- **Đường đói (FPG):** 11.2 mmol/L.\n- **Thận:** Creatinin 1.6 mg/dL (eGFR 42 mL/phút).\n- **ECG:** Dương tính khi gắng sức (ST chênh xuống lõm).",
            "question": "👉 Chẩn đoán Hội chứng vành mạn tính do biến chứng ĐTĐ lâu năm. Với eGFR 42, việc điều chỉnh thuốc hạ đường huyết nào (Metformin/SGLT2i) là an toàn và có tác dụng bảo vệ tim mạch theo phác đồ?"
        },
        {
            "name": "Lưu Văn Đ", "age": 50, "sex": "Nam", "job": "Kỹ sư", "specialty": "TIM MẠCH VÀ NỘI TIẾT",
            "reason": "Đo huyết áp lúc nào cũng 165/100, yếu cơ",
            "history": "- Uống đủ 3 nhóm thuốc hạ áp phối hợp (Amlodipin, Perindopril, Indapamide) nhưng nhức đầu bưng bưng, đo HA không hạ.\n- Cảm thấy tứ chi bủn rủn, đi lại không có lực lả người.",
            "past_medical": "- Huyết áp kháng trị 3 năm.",
            "clinical": "**Sinh hiệu:** HA đo kỹ 2 tay 168/102 mmHg.\n**Thần kinh cơ:** Trương lực cơ giảm, sức cơ tứ chi 4/5.",
            "subclinical": "- **Sinh hóa:** K+ máu tụt nghiêm trọng (2.8 mEq/L).\n- **Renin/Aldosterone:** Tỷ lệ Aldosterone/Renin (ARR) = 45 (rất cao).\n- **CT Bụng:** Khối u tuyến thượng thận trái 15mm.",
            "question": "👉 Hội chứng Conn (Cường Aldosterone tiên phát) gây huyết áp kháng trị và hạ Kali máu. Chỉ định thuốc đối kháng thụ thể Mineralocorticoid (Spironolactone) và kế hoạch can thiệp ngoại khoa?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 6: HÔ HẤP + NỘI TIẾT
    # ──────────────────────────────────────────────────────────
    "🫁+🔬 Hô hấp + Nội tiết": [
        {
            "name": "Đào Thị O", "age": 58, "sex": "Nữ", "job": "Buôn bán", "specialty": "HÔ HẤP VÀ NỘI TIẾT",
            "reason": "Ho đờm dai dẳng, đường huyết tăng vọt",
            "history": "- Đang dùng thuốc xịt Budesonide/Formoterol kiểm soát hen nhưng cơn cấp vẫn hay tái phát.\n- Mỗi lần tái phát tự ra hiệu thuốc mua Corticoid uống (Prednisolone) từ 5-7 ngày.\n- Dạo này mệt lả mồ hôi, tiểu nhiều, thèm ngọt.",
            "past_medical": "- ĐTĐ type 2 (12 năm), béo phì (BMI 33).\n- Hen dai dẳng.",
            "clinical": "**Toàn thân:** Hội chứng Cushing do thuốc (mặt tròn như mặt trăng, da mỏng).\n**Sinh hiệu:** HA 140/85 mmHg.\n**Hô hấp:** Khò khè.",
            "subclinical": "- **HbA1c:** 9.2% (Tăng cao mất kiểm soát).\n- **Khoáng xương:** Loãng xương rõ rệt T-score -2.1.",
            "question": "👉 Corticoid toàn thân điều trị Hen ảnh hưởng phá huỷ kiểm soát đường huyết và gây loãng xương. Phương án cắt giảm rủi ro Corticoid, chuyển đổi nâng bậc thuốc sinh học/ICS liều cao được đề xuất như thế nào?"
        },
        {
            "name": "Lương Hữu V", "age": 70, "sex": "Nam", "job": "Nông dân", "specialty": "HÔ HẤP VÀ NỘI TIẾT",
            "reason": "Sụt cân suy kiệt, hạ đường máu liên miên",
            "history": "- Thường xuyên ngất vì hạ đường huyết (đo ở trạm xá 3.0 mmol/L) 3 lần tuần qua.\n- Phải thở oxy tại nhà liên tục do yếu hô hấp.",
            "past_medical": "- COPD cực nặng (FEV1 32%).\n- ĐTĐ type 2 uống Metformin.",
            "clinical": "**Toàn thân:** Rất gầy mòn (BMI 17), cơ xương teo, mệt rã rời.\n**Sinh hiệu:** HA 90/60 mmHg (hạ).",
            "subclinical": "- **Đường máu:** Tuột dốc.\n- **Cortisol 8h sáng:** 2.5 μg/dL (Quá thấp).\n- **ACTH:** 85 pg/mL (Tăng cao).",
            "question": "👉 Chẩn đoán Suy thượng thận nguyên phát (Addison) trên bệnh nhân ĐTĐ/COPD. Sự thiếu hụt Cortisol phá vỡ cơ chế duy trì đường mức nào và phác đồ hydrocortisone cấp cứu?"
        }
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 7: CẢ 3 KHOA (TIM MẠCH + HÔ HẤP + NỘI TIẾT)
    # ──────────────────────────────────────────────────────────
    "🫀🫁🔬 Cả 3 khoa": [
        {
            "name": "Châu Trí P", "age": 72, "sex": "Nam", "job": "Hưu trí", "specialty": "ĐA KHOA (TIM - HÔ HẤP - NỘI TIẾT)",
            "reason": "Hôn mê, suy hô hấp nặng",
            "history": "- Ngày hôm trước có ho khạc nhiều đờm bọt hồng, nay gọi không tỉnh, người tím tái.",
            "past_medical": "- ĐTĐ type 2 (15 năm, HbA1c 8.5%).\n- Suy tim HFrEF (LVEF 30%).\n- COPD nhóm C (FEV1 42%).",
            "clinical": "**Toàn thân:** Lơ mơ không tiếp xúc.\n**Sinh hiệu:** HA 160/90 mmHg, SpO2 84%.",
            "subclinical": "- **Đường mao mạch:** 22.0 mmol/L.\n- **NT-proBNP:** 12,000 pg/mL.\n- **Khí máu:** PaCO2 55, PaO2 50, pH 7.28.\n- **X-Quang:** Phù phổi cấp.",
            "question": "👉 Ca cấp cứu phức hợp: Suy hô hấp do Phù phổi cấp, Tăng đường huyết khẩn cấp, trên nền COPD. Thiết lập thứ tự ưu tiên Điều trị 3 mũi nhọn: Đặt nội khí quản/NIV, Giảm tải tiền gánh, Insulin liên tục?"
        },
        {
            "name": "Ngô Bách T", "age": 58, "sex": "Nam", "job": "Giám đốc", "specialty": "ĐA KHOA (TIM - HÔ HẤP - NỘI TIẾT)",
            "reason": "Cơn tăng huyết áp cấp cứu, ngưng thở khi ngủ",
            "history": "- Đột ngột đau đầu chém, tức ngực, khó thở sáng sớm. Vợ bảo đêm ngủ ngáy rất to và hay ngưng thở rùng mình.",
            "past_medical": "- ĐTĐ type 2 không kiểm soát, béo phì (vòng eo 115cm).",
            "clinical": "**Sinh hiệu:** Cấp cứu HA vọt lên 220/130 mmHg.\n**Toàn thân:** Béo phì quá khổ BMI 36.",
            "subclinical": "- **Ngáy ngủ (Polysomnography):** AHI = 42 lần/giờ (Ngưng thở khi ngủ nặng).\n- **Siêu âm tim:** Phì đại thất trái đồng tâm, áp lực ĐMP tăng.\n- **Xét nghiệm:** FPG 12.5, Uric acid 520, Lipid máu cực rối loạn.",
            "question": "👉 Hội chứng chuyển hóa toàn phát có biến chứng OSAS (Ngưng thở khi ngủ cản trở) dẫn tới tăng áp ĐMP và Cơn Tăng HA. Thuốc chống tăng huyết áp đường tĩnh mạch tối ưu và chỉ định máy thở CPAP?"
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
