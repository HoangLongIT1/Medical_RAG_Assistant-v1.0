"""
sample_cases.py – Ngân hàng ca bệnh mẫu ngẫu nhiên
Tổng cộng 35 ca bệnh (5 ca × 7 nhóm chuyên khoa)
Mỗi lần nhấn nút sẽ chọn ngẫu nhiên 1 ca khác nhau.
"""

import random

# ══════════════════════════════════════════════════════════════
# NGÂN HÀNG CA BỆNH MẪU — 7 NHÓM × 5 CA = 35 CA
# ══════════════════════════════════════════════════════════════

SAMPLE_CASE_BANK = {

    # ──────────────────────────────────────────────────────────
    # NHÓM 1: TIM MẠCH (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫀 Tim mạch": [
        {
            "text": "Bệnh nhân nam 70 tuổi, tiền sử suy tim HFrEF (phân suất tống máu giảm, EF 35%). Đang dùng thuốc chẹn beta giao cảm (Bisoprolol 5mg/ngày). Hôm nay nhập viện vì nhịp tim rất chậm (40 lần/phút), huyết áp 85/50 mmHg, tay chân lạnh ẩm, khó thở nhiều khi nằm, phải ngồi thở. Điện tâm đồ cho thấy block nhĩ thất độ III. Xét nghiệm NT-proBNP tăng cao 5800 pg/mL. Có nên tiếp tục hoặc tăng liều thuốc chẹn beta cho bệnh nhân trong bối cảnh này không?",
            "age": 70, "sex": "Nam", "specialty": "Tim mạch"
        },
        {
            "text": "Bệnh nhân nữ 62 tuổi, tiền sử tăng huyết áp 10 năm, đang dùng Amlodipin 10mg và Losartan 50mg. Vào cấp cứu vì đau ngực trái dữ dội kéo dài 45 phút, đau lan lên vai trái và hàm, kèm vã mồ hôi, buồn nôn. Huyết áp 160/95 mmHg, mạch 95 lần/phút. ECG cho thấy ST chênh lên ở DII, DIII, aVF. Troponin T hs ban đầu 250 ng/L (bình thường < 14 ng/L). Bệnh nhân dị ứng Aspirin (phù mạch). Cần xử trí cấp cứu như thế nào?",
            "age": 62, "sex": "Nữ", "specialty": "Tim mạch"
        },
        {
            "text": "Bệnh nhân nam 55 tuổi đến khám vì hồi hộp, đánh trống ngực từng cơn xuất hiện 3 tháng nay, mỗi cơn kéo dài 30 phút đến vài giờ, tự hết. Kèm theo chóng mặt nhẹ khi lên cơn. Tiền sử: tăng huyết áp 5 năm, đang dùng Enalapril 10mg. Khám: HA 140/85 mmHg, mạch 82 lần/phút không đều. ECG tại phòng khám ghi nhận rung nhĩ với đáp ứng thất trung bình. Siêu âm tim: nhĩ trái giãn 42mm, EF 55%, không huyết khối. Điểm CHA2DS2-VASc là bao nhiêu và có cần dùng thuốc kháng đông không?",
            "age": 55, "sex": "Nam", "specialty": "Tim mạch"
        },
        {
            "text": "Bệnh nhân nữ 48 tuổi, béo phì (BMI 34), tiền sử gia đình có mẹ đột quỵ ở tuổi 60. Đến khám sức khỏe định kỳ, đo huyết áp 3 lần liên tiếp tại phòng khám lần lượt là: 155/98, 148/95, 152/96 mmHg. Mạch 78 lần/phút. Xét nghiệm: creatinin 1.0 mg/dL, kali 4.2 mEq/L, cholesterol toàn phần 6.5 mmol/L, LDL 4.2 mmol/L, HDL 0.9 mmol/L, đường huyết đói 5.8 mmol/L. Đáy mắt bình thường. ECG: dày thất trái (Sokolow-Lyon 38mm). Cần phân loại giai đoạn tăng huyết áp và đề xuất phác đồ điều trị ban đầu.",
            "age": 48, "sex": "Nữ", "specialty": "Tim mạch"
        },
        {
            "text": "Bệnh nhân nam 75 tuổi, tiền sử suy tim mạn EF 28% (NYHA III), bệnh mạch vành đã đặt stent LAD cách đây 3 năm, rung nhĩ vĩnh viễn. Đang dùng: Bisoprolol 2.5mg, Ramipril 5mg, Furosemide 40mg sáng, Spironolactone 25mg, Rivaroxaban 15mg. Nhập viện vì phù hai chân tăng dần 1 tuần, khó thở khi gắng sức nhẹ và khi nằm, tiểu ít. Khám: HA 100/65 mmHg, mạch 55 lần/phút, tĩnh mạch cổ nổi, ran ẩm 2 đáy phổi, gan to 3cm dưới bờ sườn, phù mềm 2 chân. Cân nặng tăng 4kg so với lần khám trước 2 tuần. Xét nghiệm: Na 128 mEq/L, K 5.6 mEq/L, creatinin 2.1 mg/dL (trước đây 1.4), BUN 45 mg/dL. Cần đánh giá tình trạng hiện tại và hướng xử trí.",
            "age": 75, "sex": "Nam", "specialty": "Tim mạch"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 2: HÔ HẤP (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫁 Hô hấp": [
        {
            "text": "Bệnh nhân nữ 65 tuổi, có tiền sử hút thuốc lá 30 gói-năm (bỏ thuốc 2 năm trước). Khám lâm sàng: khó thở khi đi bộ 100m (mMRC 2), ho khạc đờm trắng mỗi sáng. Điểm CAT là 18. Trong 12 tháng qua, bệnh nhân có 2 đợt cấp phải nhập viện điều trị, lần cuối cách đây 3 tháng. Hô hấp ký: FEV1/FVC = 0.58, FEV1 = 42% dự đoán (sau giãn phế quản). SpO2 nghỉ 93%. X-quang ngực: phổi căng giãn, cơ hoành dẹt. Cần phân loại nhóm bệnh nhân theo GOLD 2024 và hướng dẫn điều trị duy trì như thế nào?",
            "age": 65, "sex": "Nữ", "specialty": "Hô hấp"
        },
        {
            "text": "Bệnh nhân nam 58 tuổi, công nhân mỏ than 25 năm, nhập viện vì khó thở nặng lên 3 ngày, ho tăng nhiều, đờm chuyển vàng xanh, sốt 38.5°C. Tiền sử COPD 8 năm (FEV1 lần cuối 38%), đang dùng Tiotropium hít và Budesonide/Formoterol. SpO2 nhập viện 86% thở khí trời, nhịp thở 28 lần/phút, co kéo cơ hô hấp phụ. Khí máu động mạch: pH 7.32, PaCO2 58 mmHg, PaO2 52 mmHg, HCO3 28 mEq/L. X-quang phổi: tăng đậm phế trường 2 bên, không thấy hình tràn khí màng phổi. Đây là đợt cấp nặng hay rất nặng? Cần xử trí ngay như thế nào và có chỉ định thở máy không xâm lấn (NIV) không?",
            "age": 58, "sex": "Nam", "specialty": "Hô hấp"
        },
        {
            "text": "Bệnh nhân nam 45 tuổi, không hút thuốc, tiền sử viêm mũi dị ứng nhiều năm. Đến khám vì ho khan kéo dài 6 tuần, đặc biệt về đêm và sáng sớm, kèm khò khè khi tiếp xúc bụi nhà hoặc khi thay đổi thời tiết. Thỉnh thoảng cảm giác nặng ngực. Triệu chứng xuất hiện 2-3 lần/tuần, thức giấc ban đêm 2 lần/tháng. Hô hấp ký: FEV1 82% dự đoán, test phục hồi phế quản dương tính (tăng FEV1 15% và 250mL sau Salbutamol). FeNO = 45 ppb. Hemogram và X-quang phổi bình thường. Cần phân loại mức độ kiểm soát hen và đề xuất bậc điều trị theo GINA.",
            "age": 45, "sex": "Nam", "specialty": "Hô hấp"
        },
        {
            "text": "Bệnh nhân nữ 72 tuổi, nhập viện vì khó thở đột ngột xuất hiện 4 giờ trước, kèm đau ngực phải khi hít sâu. Tiền sử: phẫu thuật thay khớp háng phải cách đây 10 ngày, nằm bất động tại giường phần lớn thời gian. BMI 32. Khám: mạch 110 lần/phút, HA 100/70 mmHg, nhịp thở 26 lần/phút, SpO2 90%. Phổi trong. Chân phải sưng hơn chân trái. D-dimer > 5000 ng/mL. ECG: nhịp nhanh xoang, trục phải, S1Q3T3. Khí máu: PaO2 62 mmHg, PaCO2 30 mmHg. Điểm Wells là bao nhiêu và cần chẩn đoán xác định bằng phương pháp nào?",
            "age": 72, "sex": "Nữ", "specialty": "Hô hấp"
        },
        {
            "text": "Bệnh nhân nam 35 tuổi, nhân viên văn phòng, đến khám vì ho có đờm trắng kéo dài 4 tuần, kèm sốt nhẹ về chiều (37.5-38°C), ra mồ hôi trộm ban đêm, sụt 5kg trong 1 tháng. Tiền sử: tiếp xúc với đồng nghiệp được chẩn đoán lao phổi 2 tháng trước. Khám: thể trạng gầy, phổi nghe ran nổ vùng đỉnh phổi phải. X-quang phổi: thâm nhiễm đỉnh phổi phải với hình hang nhỏ. Xét nghiệm máu: bạch cầu 9500, lympho 35%, CRP 35 mg/L, VS 55mm/h. Xét nghiệm HIV âm tính. Cần làm gì để chẩn đoán xác định và phác đồ điều trị nếu xác nhận lao phổi mới?",
            "age": 35, "sex": "Nam", "specialty": "Hô hấp"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 3: NỘI TIẾT - CHUYỂN HÓA (5 ca)
    # ──────────────────────────────────────────────────────────
    "🔬 Nội tiết": [
        {
            "text": "Bệnh nhân nam 45 tuổi, nhân viên văn phòng, BMI 27.5, đi khám sức khỏe định kỳ. Kết quả xét nghiệm: đường huyết đói (FPG) là 7.5 mmol/L (lần 1), xét nghiệm lặp lại sau 1 tuần FPG = 7.8 mmol/L. HbA1c là 6.8%. Bệnh nhân không có triệu chứng kinh điển của đái tháo đường (không ăn nhiều, uống nhiều, tiểu nhiều, sụt cân). Tiền sử gia đình: bố mắc ĐTĐ type 2 từ tuổi 50. Cholesterol toàn phần 5.8 mmol/L, LDL 3.5 mmol/L, triglyceride 2.8 mmol/L. HA 135/85 mmHg. Creatinin 0.9 mg/dL, MAU (microalbumin niệu) 45 mg/g creatinin. Hỏi bệnh nhân này đã đủ tiêu chuẩn chẩn đoán ĐTĐ type 2 chưa? Cần chiến lược điều trị ban đầu ra sao?",
            "age": 45, "sex": "Nam", "specialty": "Nội tiết - Chuyển hóa"
        },
        {
            "text": "Bệnh nhân nữ 52 tuổi, ĐTĐ type 2 phát hiện 8 năm, đang dùng Metformin 2000mg/ngày và Gliclazide MR 60mg/ngày. HbA1c hiện tại 8.5% (mục tiêu < 7%). BMI 31, vòng eo 98cm. Creatinin 1.3 mg/dL, eGFR 52 mL/phút (suy thận mạn giai đoạn 3a). MAU 180 mg/g creatinin. Tiền sử nhồi máu cơ tim cách đây 2 năm, đang dùng Aspirin, Atorvastatin 40mg, Bisoprolol 5mg. HA 145/90 mmHg. Mắt: bệnh võng mạc ĐTĐ không tăng sinh 2 mắt. Bàn chân: giảm cảm giác rung âm thoa 2 bàn chân, monofilament âm tính ngón 1 và ngón 5 chân phải. Cần điều chỉnh phác đồ điều trị ĐTĐ như thế nào trong bối cảnh nhiều bệnh đồng mắc?",
            "age": 52, "sex": "Nữ", "specialty": "Nội tiết - Chuyển hóa"
        },
        {
            "text": "Bệnh nhân nam 28 tuổi, nhập cấp cứu trong tình trạng lơ mơ, thở nhanh sâu kiểu Kussmaul. Người nhà cho biết bệnh nhân ĐTĐ type 1 từ 15 tuổi, đang dùng insulin Lantus 20 đơn vị buổi tối + insulin Novorapid trước bữa ăn. 3 ngày trước bệnh nhân bị viêm họng sốt cao và tự ý ngưng tiêm insulin vì ăn ít. Khám: lơ mơ (GCS 12), thở Kussmaul 30 lần/phút, hơi thở mùi trái cây, mạch 120 lần/phút, HA 90/60 mmHg, da khô, turgor giảm. Xét nghiệm: đường huyết 28 mmol/L, pH 7.08, HCO3 6 mEq/L, PaCO2 18 mmHg, Na 130 mEq/L, K 5.8 mEq/L, ketone máu 6.2 mmol/L, creatinin 1.8 mg/dL, lactate 3.5 mmol/L, bạch cầu 18000 (N 85%). Chẩn đoán và xử trí cấp cứu theo phác đồ?",
            "age": 28, "sex": "Nam", "specialty": "Nội tiết - Chuyển hóa"
        },
        {
            "text": "Bệnh nhân nữ 38 tuổi, đến khám vì sụt cân 8kg trong 3 tháng dù ăn nhiều, kèm hồi hộp, run tay, ra mồ hôi nhiều, đi tiêu lỏng 3-4 lần/ngày, kinh nguyệt thưa. Khám: mạch 105 lần/phút (nghỉ), HA 145/60 mmHg, bướu giáp lan tỏa độ II, sờ mềm, không đau, có rung miu. Mắt: lồi mắt 2 bên (Hertel 22mm), co trợn mi trên, hở mi khi nhắm mắt. Run đầu chi. Phản xạ gân xương tăng. Xét nghiệm: TSH < 0.01 mIU/L, FT4 = 52 pmol/L (bt 12-22), FT3 = 18 pmol/L (bt 3.1-6.8), TRAb = 15 IU/L (bt < 1.75). Công thức máu: bạch cầu 4200, bạch cầu hạt 1800. Chẩn đoán xác định bệnh gì? Có chống chỉ định gì khi dùng thuốc kháng giáp tổng hợp?",
            "age": 38, "sex": "Nữ", "specialty": "Nội tiết - Chuyển hóa"
        },
        {
            "text": "Bệnh nhân nam 60 tuổi, ĐTĐ type 2 điều trị 12 năm, đang dùng insulin premixed (Mixtard 30) 30 đơn vị sáng + 20 đơn vị tối. Đến khám vì hay bị hạ đường huyết vào lúc 3-4 giờ sáng (ra mồ hôi, run, đánh trống ngực, người nhà phát hiện bệnh nhân vật vã trong giấc ngủ). Theo dõi đường huyết mao mạch 7 ngày: đường huyết trước ăn sáng dao động 4.5-12 mmol/L, trước ăn trưa 3.2-5.5 mmol/L, trước ăn tối 8-15 mmol/L, 3 giờ sáng có 2 lần đo được 2.8 và 3.1 mmol/L. HbA1c 7.8%. BMI 25. Creatinin 1.5 mg/dL, eGFR 45 mL/phút. Bệnh nhân có bệnh lý thần kinh tự chủ (không nhận biết triệu chứng hạ đường huyết khi tỉnh). Cần chuyển đổi phác đồ insulin như thế nào để giảm nguy cơ hạ đường huyết ban đêm?",
            "age": 60, "sex": "Nam", "specialty": "Nội tiết - Chuyển hóa"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 4: TIM MẠCH + HÔ HẤP (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫀+🫁 Tim + Hô hấp": [
        {
            "text": "Bệnh nhân nam 68 tuổi, tiền sử COPD (GOLD D) và suy tim mạn EF 40%. Đang dùng Tiotropium, Budesonide/Formoterol, Bisoprolol 2.5mg, Ramipril 5mg, Furosemide 40mg. Vào viện vì khó thở dữ dội, vã mồ hôi, ngồi thở. Ho khạc đờm trắng bọt, không sốt. Khám: HA 170/100 mmHg, mạch 115 lần/phút, SpO2 85%. Phổi: ran rít, ran ngáy rải rác và ran ẩm ở hai đáy phổi. Tĩnh mạch cổ nổi. Siêu âm tim nhanh tại giường: thành trước thất trái giảm động, LVEF 35%. NT-proBNP 6500 pg/mL. Khí máu: pH 7.35, PaCO2 48, PaO2 55, HCO3 26. Nguyên nhân chính gây khó thở đợt này là đợt cấp COPD hay phù phổi cấp do suy tim? Hướng xử trí ban đầu?",
            "age": 68, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 74 tuổi, tiền sử rung nhĩ vĩnh viễn đang dùng Rivaroxaban 15mg, suy tim EF bảo tồn (HFpEF, EF 58%), bệnh phổi tắc nghẽn mạn tính (COPD nhóm B). Đến khám vì khó thở tăng dần 2 tuần, phù 2 mắt cá chân, ho khan về đêm. Đang dùng Tiotropium hít, Amlodipine 5mg. Khám: HA 155/90 mmHg, mạch 95 lần/phút không đều, SpO2 91%, ran ẩm ít 2 đáy phổi, phù mềm 2 chân. BNP 450 pg/mL. Hô hấp ký gần nhất: FEV1 55% dự đoán. X-quang: bóng tim to, tái phân bố tuần hoàn phổi. Đây là đợt cấp suy tim hay đợt cấp COPD? Thuốc nào cần điều chỉnh?",
            "age": 74, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 66 tuổi, hút thuốc 40 gói-năm, tiền sử tăng huyết áp và COPD. Nhập viện vì đau ngực trái lan ra lưng kéo dài 2 giờ kèm khó thở tăng dần. Đang dùng Salmeterol/Fluticasone hít, Amlodipine 10mg, Atorvastatin 20mg. Khám: HA 180/110 mmHg, mạch 100 lần/phút, SpO2 88%, phổi ran rít 2 bên kèm ran ẩm đáy phổi phải. ECG: ST chênh xuống V4-V6, T âm sâu V1-V3. Troponin T hs 89 ng/L (bình thường < 14). Khí máu: pH 7.38, PaCO2 42, PaO2 58. D-dimer 800 ng/mL. Cần chẩn đoán phân biệt giữa hội chứng vành cấp, đợt cấp COPD và thuyên tắc phổi. Hướng tiếp cận chẩn đoán và xử trí?",
            "age": 66, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 60 tuổi, tiền sử suy tim HFrEF (EF 30%) sau nhồi máu cơ tim thành trước 5 năm trước, COPD nhóm B (FEV1 60%). Đang dùng: Carvedilol 6.25mg × 2, Sacubitril/Valsartan 50mg × 2, Spironolactone 25mg, Furosemide 20mg, Tiotropium hít. Đến tái khám vì ho khan kéo dài 1 tháng nay, không sốt, khó thở ổn định (mMRC 1-2). BNP ổn định 280 pg/mL. Hô hấp ký: FEV1 không thay đổi so với trước. X-quang phổi: không tổn thương mới. Nguyên nhân ho khan có thể do thuốc nào? Cần điều chỉnh gì?",
            "age": 60, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 78 tuổi, tiền sử bệnh mạch vành mạn đã phẫu thuật bắc cầu chủ vành (CABG) 8 năm trước, COPD nhóm C (FEV1 45%), rung nhĩ. Nhập viện vì ngất thoáng qua khi đi vệ sinh, kèm khó thở tăng dần 5 ngày, phù chân. Đang dùng: Aspirin 81mg, Warfarin (INR mục tiêu 2-3), Digoxin 0.125mg, Furosemide 80mg, Tiotropium, Budesonide/Formoterol. Khám: HA 105/65 mmHg, mạch 50 lần/phút (chậm, không đều), SpO2 90%, tĩnh mạch cổ nổi, ran ẩm 2/3 dưới 2 phổi, phù chân 2 bên. ECG: rung nhĩ đáp ứng thất chậm 50/phút, ST chênh xuống lan tỏa. Xét nghiệm: Digoxin máu 3.2 ng/mL (bình thường 0.5-2.0), INR 4.5, K 5.8, creatinin 2.3 mg/dL. Cần đánh giá nguyên nhân ngất và xử trí cấp?",
            "age": 78, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 5: TIM MẠCH + NỘI TIẾT (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫀+🔬 Tim + Nội tiết": [
        {
            "text": "Bệnh nhân nữ 55 tuổi, tiền sử tăng huyết áp 5 năm đang điều trị Amlodipin 10mg. Gần đây ăn nhiều, hay khát nước và sụt 3kg/tháng. Xét nghiệm: HbA1c 7.2%, FPG 8.1 mmol/L, cholesterol toàn phần 6.8 mmol/L, LDL 4.5 mmol/L, triglyceride 3.2 mmol/L. Khám tim: có tiếng ngựa phi T3, siêu âm tim LVEF 45% (giảm nhẹ), giãn nhĩ trái 44mm, E/e' = 14, tĩnh mạch cổ nổi nhẹ. ECG: phì đại thất trái, ST chênh xuống nhẹ V5-V6. Creatinin 1.1 mg/dL, MAU 120 mg/g creatinin. Cần chẩn đoán xác định các bệnh lý nào trên bệnh nhân này và đề xuất phác đồ điều trị toàn diện?",
            "age": 55, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 63 tuổi, ĐTĐ type 2 (10 năm), tăng huyết áp (8 năm), rối loạn lipid máu. Đang dùng: Metformin 2000mg, Gliclazide 60mg, Losartan 100mg, Hydrochlorothiazide 25mg, Atorvastatin 40mg. Nhập viện vì đau ngực khi gắng sức xuất hiện từ 2 tuần nay (đau thắt ngực ổn định CCS II), kèm khó thở nhẹ. HA 150/95 mmHg, mạch 88 lần/phút. HbA1c 8.8%, FPG 11.2 mmol/L. Creatinin 1.6 mg/dL, eGFR 42 mL/phút. K 5.1 mEq/L. ECG gắng sức: dương tính (ST chênh xuống 2mm ở V4-V6 tại tần số tim 120). Siêu âm tim: EF 50%, giảm động thành dưới. Cần hướng tiếp cận chẩn đoán mạch vành và điều chỉnh phác đồ ĐTĐ trong bối cảnh bệnh mạch vành + suy thận?",
            "age": 63, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 70 tuổi, tiền sử ĐTĐ type 2 (20 năm), suy tim HFpEF (EF 55%), tăng huyết áp, béo phì (BMI 35). Đang dùng: Insulin Glargine 30 đơn vị/tối, Metformin 1500mg, Furosemide 40mg, Spironolactone 25mg, Perindopril 5mg, Amlodipin 5mg. Nhập viện vì phù tăng 2 chân, khó thở khi gắng sức (NYHA III), tăng cân 3kg/2 tuần. HbA1c 7.0%. Na 132 mEq/L, K 4.8 mEq/L. NT-proBNP 1800 pg/mL. Creatinin 1.4 mg/dL, eGFR 38 mL/phút. Có nên dùng thuốc SGLT2 inhibitor (Empagliflozin/Dapagliflozin) trong trường hợp này không? Cần cân nhắc những gì?",
            "age": 70, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 50 tuổi, tiền sử tăng huyết áp khó kiểm soát 3 năm (HA trung bình 165/100 mmHg dù đã dùng 3 thuốc: Amlodipin 10mg + Perindopril 10mg + Indapamide 1.5mg). Gần đây phát hiện thêm đường huyết đói 6.5 mmol/L, K máu 2.8 mEq/L (hạ kali liên tục dù không dùng lợi tiểu thải kali mạnh). BMI 26. Xét nghiệm: Aldosterone/Renin ratio (ARR) = 45 (bình thường < 30), aldosterone huyết tương 25 ng/dL. CT scan bụng: u tuyến thượng thận trái kích thước 15mm, đồng nhất, mật độ thấp. Cần nghĩ đến bệnh lý nào gây tăng huyết áp thứ phát? Cần xét nghiệm xác nhận gì thêm?",
            "age": 50, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 45 tuổi, nhập cấp cứu vì rung thất (được sốc điện chuyển nhịp thành công ngoại viện). Tiền sử: cường giáp Basedow phát hiện 6 tháng, đang dùng Methimazole 20mg/ngày nhưng bệnh nhân tự ý giảm liều xuống 5mg/ngày do sợ tác dụng phụ. Khám: mạch 140 lần/phút (rung nhĩ đáp ứng thất nhanh), HA 160/60 mmHg, sốt 38.8°C, kích thích vật vã, run tay thô, bướu giáp to, lồi mắt. Xét nghiệm: TSH < 0.01, FT4 = 85 pmol/L, FT3 = 32 pmol/L. Troponin T 45 ng/L. K 3.0 mEq/L, Ca 2.65 mmol/L. Men gan: AST 120, ALT 95. Bệnh nhân có thể đang trong tình trạng gì? Cần xử trí cấp cứu ra sao?",
            "age": 45, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 6: HÔ HẤP + NỘI TIẾT (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫁+🔬 Hô hấp + Nội tiết": [
        {
            "text": "Bệnh nhân nam 62 tuổi, hút thuốc 20 gói-năm (đã bỏ 1 năm), BMI 29, vòng eo 102cm. Đến khám vì ho có đờm trắng kéo dài 4 tuần, khó thở nhẹ khi leo cầu thang (mMRC 1). Khám sức khỏe tình cờ phát hiện đường máu đói 8.5 mmol/L và HbA1c 7.5%, chưa có chẩn đoán ĐTĐ trước đây. Hô hấp ký: FEV1/FVC = 0.65, FEV1 = 72% dự đoán (sau test phục hồi phế quản: tăng 8% và 150mL — âm tính). SpO2 94%. X-quang phổi: phổi ứ khí, không thâm nhiễm. Triglyceride 3.5 mmol/L, LDL 3.8 mmol/L. HA 140/88 mmHg. Bệnh nhân có đồng thời COPD và ĐTĐ type 2 mới phát hiện không? Cần chiến lược điều trị phối hợp ra sao?",
            "age": 62, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 58 tuổi, ĐTĐ type 2 (12 năm), béo phì (BMI 33), hen phế quản dai dẳng mức độ trung bình. Đang dùng: Metformin 2000mg, Sitagliptin 100mg, Insulin Glargine 25 đơn vị, Budesonide/Formoterol 200/6 μg × 2 nhát/ngày. Bệnh nhân thường xuyên phải dùng corticoid uống (Prednisolone 30mg × 5-7 ngày) cho các đợt cấp hen (4 lần trong năm qua). HbA1c 9.2%. Đường huyết dao động lớn 5-22 mmol/L. Mật độ xương DEXA: T-score cột sống -2.1. Cần đánh giá ảnh hưởng của corticoid lên kiểm soát đường huyết và đề xuất chiến lược giảm phụ thuộc corticoid toàn thân?",
            "age": 58, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 55 tuổi, COPD (GOLD C, FEV1 40%), ĐTĐ type 2 (HbA1c 8.0%), đang dùng Metformin 1700mg + Empagliflozin 10mg + Tiotropium + Budesonide/Formoterol. Nhập viện vì đợt cấp COPD (ho tăng, đờm vàng xanh, sốt 38.2°C, khó thở tăng). SpO2 88%. Được điều trị với kháng sinh, giãn phế quản nebulizer, và Prednisolone 40mg/ngày × 5 ngày. Ngày thứ 2: đường huyết mao mạch tăng vọt 18-25 mmol/L. Bệnh nhân khai uống đủ thuốc ĐTĐ. Nguyên nhân tăng đường huyết đột ngột? Cần xử trí đường huyết như thế nào trong bối cảnh đợt cấp COPD đang dùng corticoid?",
            "age": 55, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 65 tuổi, tiền sử cường giáp Basedow (đang dùng Methimazole 10mg), COPD nhẹ-trung bình (FEV1 65%). Đến khám vì khó thở tăng dần 1 tháng, hồi hộp, sụt 4kg. Mạch 110 lần/phút, HA 150/60 mmHg. Phổi: ran rít nhẹ 2 bên. Xét nghiệm: TSH < 0.05 mIU/L, FT4 = 35 pmol/L (cao). Hô hấp ký: FEV1 giảm từ 65% xuống 52% so với 6 tháng trước. SpO2 92%. ECG: rung nhĩ đáp ứng thất nhanh 120/phút. Nguyên nhân khó thở tăng dần là do COPD tiến triển hay cường giáp không kiểm soát gây ảnh hưởng đến chức năng hô hấp và tim mạch? Cần xử trí gì trước?",
            "age": 65, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 70 tuổi, COPD nặng (FEV1 32%), thở oxy tại nhà 2L/phút liên tục, ĐTĐ type 2 (HbA1c 7.5%), suy dinh dưỡng (BMI 17.5, albumin 2.8 g/dL). Đang dùng: Tiotropium + Umeclidinium/Vilanterol, Insulin Glargine 12 đơn vị, Metformin 500mg × 2. Tới khám vì mệt mỏi tăng dần, yếu cơ tứ chi, hay bị hạ đường huyết (3 lần/tuần, đường huyết đo được 3.0-3.5 mmol/L). Cân nặng giảm thêm 2kg/tháng qua. Cortisol 8 giờ sáng: 2.5 μg/dL (bình thường 6-23). ACTH 85 pg/mL (cao). Na 128 mEq/L, K 5.5 mEq/L. Cần nghĩ đến bệnh lý nào ngoài ĐTĐ và COPD? Cần đánh giá thêm gì?",
            "age": 70, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
    ],

    # ──────────────────────────────────────────────────────────
    # NHÓM 7: TIM MẠCH + HÔ HẤP + NỘI TIẾT (5 ca)
    # ──────────────────────────────────────────────────────────
    "🫀🫁🔬 Cả 3 khoa": [
        {
            "text": "Bệnh nhân nam 72 tuổi, ĐTĐ type 2 (15 năm, HbA1c 8.5%), suy tim mạn LVEF 30% (NYHA III, đang dùng Bisoprolol 5mg, Enalapril 10mg, Spironolactone 25mg, Furosemide 80mg), COPD nhóm C (FEV1 42%, đang dùng Tiotropium + ICS/LABA). Nhập viện vì khó thở kịch phát về đêm, ho có đờm bọt hồng, SpO2 84% thở khí trời. HA 160/90 mmHg, mạch 105 lần/phút không đều. Đường huyết mao mạch 22 mmol/L. Khí máu: pH 7.28, PaCO2 55, PaO2 50, HCO3 24, Lactate 4.2. NT-proBNP 12000 pg/mL. X-quang: phù phổi cấp + bóng tim to. Ceton máu 0.5 mmol/L. Chẩn đoán nào là chính cho tình trạng cấp cứu này và thứ tự ưu tiên xử trí?",
            "age": 72, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 68 tuổi, tiền sử bệnh mạch vành mạn (đặt 2 stent LAD và RCA 4 năm trước), ĐTĐ type 2 (HbA1c 7.8%), COPD nhóm B (FEV1 58%), tăng huyết áp. Đang dùng: Aspirin 81mg, Clopidogrel 75mg, Atorvastatin 40mg, Metformin 1500mg, Empagliflozin 10mg, Losartan 100mg, Nebivolol 5mg, Tiotropium hít. Đến khám tái khám vì khó thở tăng nhẹ khi leo 1 tầng lầu (trước đây leo 2 tầng mới mệt), phù nhẹ 2 mắt cá chân, mệt mỏi hơn. HA 130/80, mạch 62/phút. SpO2 93%. Siêu âm tim: EF giảm từ 50% xuống 42%, E/e' = 16, giãn nhĩ trái. BNP 680 pg/mL. Hô hấp ký: FEV1 ổn định. Creatinin 1.3, eGFR 48, K 4.9. Đánh giá nguyên nhân suy giảm chức năng và cần điều chỉnh phác đồ gì?",
            "age": 68, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 75 tuổi, tiền sử nhồi máu cơ tim cũ (EF 35%), rung nhĩ (dùng Warfarin), ĐTĐ type 2 (dùng Insulin), COPD nặng (FEV1 35%, thở oxy tại nhà). Nhập ICU vì viêm phổi nặng cộng đồng. Hiện đang thở máy xâm lấn ngày thứ 5. Đường huyết dao động 4-25 mmol/L dù dùng insulin truyền tĩnh mạch. INR 5.2 (mục tiêu 2-3). Creatinin tăng từ 1.5 lên 2.8 mg/dL. K 5.9 mEq/L. Troponin I tăng 350 ng/L. ECG: rung nhĩ + ST chênh xuống lan tỏa. Huyết động: HA 90/55 dù đã dùng Norepinephrine 0.15 μg/kg/phút. Procalcitonin 8.5 ng/mL. Lactate 4.8 mmol/L. Cần đánh giá tất cả các vấn đề cấp và xếp thứ tự ưu tiên xử trí.",
            "age": 75, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nữ 64 tuổi, ĐTĐ type 2 (18 năm), suy tim HFrEF (EF 32%), COPD nhóm D (FEV1 38%), bệnh thận mạn giai đoạn 4 (eGFR 22 mL/phút). Đang dùng: Insulin Lantus 35 đơn vị + Novorapid trước ăn, Carvedilol 12.5mg × 2, Sacubitril/Valsartan 50mg × 2, Furosemide 80mg × 2, Tiotropium + Budesonide/Formoterol. Đến tái khám: cân nặng tăng 5kg/tháng, khó thở NYHA IV, SpO2 87%, phù toàn thân, HA 100/60, mạch 88, ran ẩm toàn bộ 2 phổi. HbA1c 8.2%, K 6.2, Na 126, Hb 8.5 g/dL, creatinin 3.8 mg/dL. Cần đánh giá toàn diện và xử trí các vấn đề nào trước? Có chỉ định lọc máu cấp cứu không?",
            "age": 64, "sex": "Nữ", "specialty": "Tự động nhận diện"
        },
        {
            "text": "Bệnh nhân nam 58 tuổi, mới phát hiện ĐTĐ type 2 (FPG 12.5 mmol/L, HbA1c 10.2%), béo phì (BMI 36, vòng eo 115cm), tăng huyết áp mới (HA 165/100 mmHg đo 3 lần), ngưng thở khi ngủ nặng (AHI = 42 sự kiện/giờ, SpO2 tối thiểu 72% khi ngủ). Nhập viện vì cơn tăng huyết áp cấp cứu (HA 220/130 mmHg) kèm khó thở, đau đầu dữ dội sáng sớm. Khám: SpO2 thức 91%, ngủ gật ban ngày nhiều (Epworth 18/24). ECG: dày thất trái, QTc kéo dài 480ms. Siêu âm tim: EF 48%, phì đại đồng tâm thất trái, áp lực ĐMP tăng 45 mmHg. Triglyceride 5.8 mmol/L, HDL 0.7 mmol/L. Acid uric 520 μmol/L. ALT 68. Đây là hội chứng chuyển hóa nặng kèm OSA. Cần tiếp cận điều trị toàn diện như thế nào?",
            "age": 58, "sex": "Nam", "specialty": "Tự động nhận diện"
        },
    ],
}

# ── Danh sách nhóm theo thứ tự hiển thị ─────────────────────
CATEGORY_ORDER_ROW1 = ["🫀 Tim mạch", "🫁 Hô hấp", "🔬 Nội tiết"]
CATEGORY_ORDER_ROW2 = ["🫀+🫁 Tim + Hô hấp", "🫀+🔬 Tim + Nội tiết", "🫁+🔬 Hô hấp + Nội tiết", "🫀🫁🔬 Cả 3 khoa"]


def get_random_case(category: str) -> dict:
    """
    Chọn ngẫu nhiên 1 ca bệnh từ nhóm chuyên khoa.
    Đảm bảo không trùng với ca đã chọn trước đó (nếu có thể).
    """
    cases = SAMPLE_CASE_BANK.get(category, [])
    if not cases:
        return {"text": "", "age": 0, "sex": "Nam", "specialty": "Tự động nhận diện"}
    return random.choice(cases)
