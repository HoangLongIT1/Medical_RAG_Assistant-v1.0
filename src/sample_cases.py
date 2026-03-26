"""
sample_cases.py – Ngân hàng ca bệnh mẫu ngẫu nhiên
Gồm 40 ca bệnh (10 ca/nhóm) được định dạng chuẩn Bệnh án Nội khoa Lâm sàng.
Chỉ giữ lại 4 chuyên khoa: Tim mạch, Hô hấp, Nội tiết, Răng Hàm Mặt.
Chi tiết, sắc bén, bám sát thực tế phòng cấp cứu và phòng khám.
"""

import random

def format_case(case_data: dict) -> str:
    name = case_data.get('name', 'Bệnh nhân')
    sex = "nam giới" if case_data['sex'].lower() == "nam" else "nữ giới"
    age = case_data['age']
    job = case_data.get('job', 'Lao động tự do').lower()
    
    pronoun = "Bệnh nhân"
    if age >= 60:
        pronoun = "Ông" if sex == "nam giới" else "Bà"
    elif age <= 15: 
        pronoun = "Cháu"
    elif sex == "nam giới": 
        pronoun = "Anh"
    else: 
        pronoun = "Chị"

    reason = case_data['reason'].strip()
    if reason and reason[0].isupper():
        reason = reason[0].lower() + reason[1:]

    history = case_data['history'].strip(" -")
    past_medical = case_data['past_medical'].strip(" -")
    
    clinical = case_data['clinical'].replace('**', '').replace('\n', ' ').strip()
    subclinical = case_data['subclinical'].replace('**', '').replace('\n', '; ').replace('- ', '').strip()
    question = case_data['question'].replace('👉', '').strip()

    template = f"""{pronoun} {name}, {sex}, {age} tuổi, công việc hiện tại là {job}, đến khám tại viện vào ngày 26/03/2026. 

{pronoun} nhập viện với lý do chính là {reason}

Theo bệnh sử, {history} Về tiền sử y khoa, {pronoun.lower()} có ghi nhận: {past_medical}

Qua quá trình thăm khám lâm sàng tuyến đầu, bác sĩ điều trị ghi nhận các dấu hiệu: {clinical} 

Kết quả cận lâm sàng được thực hiện cho thấy: {subclinical}

Dựa trên toàn bộ thông tin bệnh án này, yêu cầu hệ thống RAG phân tích: {question}"""
    return template

SAMPLE_CASE_BANK = {
    "🫀 Tim mạch": [
        {
            "name": "Trần Văn Sáng", "age": 62, "sex": "Nam", "job": "Nông dân", "specialty": "TIM MẠCH",
            "reason": "Đau tức ngực trái dữ dội lan ra sau lưng, vã mồ hôi 2 giờ.",
            "history": "- Đột ngột xuất hiện cơn đau ngực trái sau bữa ăn tối, cảm giác như bị bóp nghẹt. Kèm theo khó thở, buồn nôn, vã mồ hôi hột. Đau kéo dài liên tục không giảm khi nghỉ ngơi hay ngậm Nitroglycerin tự mua.",
            "past_medical": "- Tăng huyết áp 10 năm (HA max 180/100) đang dùng Amlodipine 5mg/ngày nhưng không đều. Sinh hoạt: Hút thuốc lào 20 năm.",
            "clinical": "**Sinh hiệu:** Mạch 110 l/p, HA 160/95 mmHg, SpO2 94% khí trời.\n**Toàn thân:** Vật vã kích thích, da niêm mạc nhợt.\n**Tim mạch:** Nhịp tim đều, T1 T2 rõ, không âm thổi. Tĩnh mạch cổ không nổi.",
            "subclinical": "- **ECG:** ST chênh lên rõ rệt ở các chuyển đạo V1-V4, sóng Q bệnh lý V1-V3.\n- **Men tim:** Troponin hs-T tăng vọt ở mức 1520 ng/L.\n- **Siêu âm tim:** Giảm động thành trước, LVEF 45%.",
            "question": "👉 Nhồi máu cơ tim cấp có ST chênh lên (STEMI) thành trước rộng giờ thứ 2. Vui lòng đưa ra Phác đồ tái tưới máu cấp cứu và các thuốc chống huyết khối mẻ đầu tiên theo khuyến cáo BYT."
        },
        {
            "name": "Lê Thị Bích", "age": 75, "sex": "Nữ", "job": "Cán bộ hưu", "specialty": "TIM MẠCH",
            "reason": "Khó thở thành cơn về đêm, phù hai chân tăng dần.",
            "history": "- Khoảng 1 tháng nay bệnh nhân thấy mệt nhiều khi leo cầu thang. 1 tuần nay phải kê 3 gối để ngủ. Hôm qua đang ngủ phải ngồi dậy thở ngháp cá. Kèm phù cẳng chân 2 bên, tiểu ít (khoảng 600ml/ngày).",
            "past_medical": "- Hẹp hở van 2 lá do thấp tim từ thời trẻ, đã nong van cách 15 năm. Rung nhĩ mạn tính đang dùng Sintrom 2mg.",
            "clinical": "**Sinh hiệu:** Mạch 120 l/p (loạn nhịp hoàn toàn), HA 110/70 mmHg, SpO2 90%.\n**Lâm sàng:** Phù mềm ấn lõm hai chi dưới. Phổi rải rác ran ẩm hai đáy. Gan to dưới bờ sườn 2cm, ấn phản hồi gan - TM cổ dương tính.",
            "subclinical": "- **X-quang:** Bóng tim to, chỉ số tim/lồng ngực 0.65, ứ huyết phổi.\n- **Siêu âm tim:** Hẹp hở van 2 lá khít, diện tích lỗ van ống 1.1 cm2. Huyết khối tiểu nhĩ trái 15x20mm.\n- **INR:** 1.5 (không đạt mục tiêu).",
            "question": "👉 Đợt mất bù cấp của Suy tim mạn trên nền bệnh van tim & rung nhĩ có huyết khối. Bệnh nhân có chỉ định dùng thuốc lợi tiểu quai liều nào và chiến lược kiểm soát đông máu ra sao?"
        },
        {
            "name": "Ngô Hoàng", "age": 45, "sex": "Nam", "job": "Giám đốc", "specialty": "TIM MẠCH",
            "reason": "Khám sức khỏe định kỳ phát hiện mỡ máu cao, thỉnh thoảng đau ngực trái.",
            "history": "- Bệnh nhân làm việc căng thẳng, đi nhậu nhiều. Đôi khi tức ngực trái tự thoáng qua khoảng 3-5 phút khi xách nặng hoặc leo dốc, nghỉ thì hết. Không khó thở.",
            "past_medical": "- Béo phì độ 1 (BMI 28.5). Rối loạn lipid máu nhiều năm chưa can thiệp.",
            "clinical": "**Sinh hiệu:** Mạch 80 l/p, HA 135/85 mmHg.\n**Toàn thân:** Ban vàng (xanthelasma) nhỏ mi mắt hai bên.\n**Tim mạch:** Bình thường.",
            "subclinical": "- **Sinh hóa máu:** Cholesterol TP 7.2 mmol/L, LDL-C 5.1 mmol/L, Triglycerid 4.5 mmol/L.\n- **Đường huyết đói:** 6.1 mmol/L.\n- **Nghiệm pháp gắng sức điện tâm đồ:** Dương tính (ST chênh xuống 1.5mm ở V4-V6 khi đạt 85% nhịp tim tối đa).",
            "question": "👉 Suy vành mạn tính (Hội chứng vành mạn) trên bệnh nhân béo phì, rối loạn lipid máu hỗn hợp. Xin đề xuất phác đồ statin liều cao và các chỉ định cận lâm sàng chụp mạch vành tiếp theo."
        },
        {
            "name": "Hoàng Tuyết O", "age": 82, "sex": "Nữ", "job": "Nội trợ", "specialty": "TIM MẠCH",
            "reason": "Ngất xỉu đột ngột đang đi chợ.",
            "history": "- Cùng ngày khám, bệnh nhân đang xách giỏ đi bộ thì thấy tối sầm mặt mũi và ngã ra đất, mất ý thức khoảng 15 giây, tỉnh lại tự đứng lên được. Không co giật, không ị đái dầm. Gần đây hay cám giác hụt hẫng nhịp tim.",
            "past_medical": "- Suy nút xoang nhẹ đã ghi nhận. Thoái hóa đa khớp.",
            "clinical": "**Sinh hiệu:** Mạch chậm 40 l/p, HA 150/60 mmHg (huyết áp mạch kẹt).\n**Tim mạch:** T1 đanh, nhịp rất thưa thớt.\n**Thần kinh:** Khám không có dấu hiệu thần kinh khu trú.",
            "subclinical": "- **ECG lúc vào viện:** Block nhĩ thất cấp III (AV Block type 3), tần số thất 38 chu kỳ/phút, sóng P không dẫn.\n- **Điện giải đồ:** K+ 4.0 (bình thường).",
            "question": "👉 Cơn Adams-Stokes do Block nhĩ thất độ III. Có cần đặt máy tạo nhịp tạm thời cấp cứu không? Phác đồ điều trị nội khoa tạm thời trong lúc chờ đặt máy?"
        },
        {
            "name": "Phan Hữu Q", "age": 55, "sex": "Nam", "job": "Lái xe", "specialty": "TIM MẠCH",
            "reason": "Choáng váng, hồi hộp trống ngực liên hồi kéo dài 4 tiếng.",
            "history": "- Xuất hiện cơn đánh trống ngực đập thình thịch liên hồi sau uống 3 ly cà phê đặc. Mệt ngực, choáng váng nhẹ nhưng chưa ngất.",
            "past_medical": "- Hội chứng Wolff-Parkinson-White (WPW) phát hiện tình cờ 5 năm trước chưa cắt đốt.",
            "clinical": "**Sinh hiệu:** Mạch RẤT NHANH 180 l/p, HA 100/65 mmHg.\n**Tim mạch:** Nhịp đập quá nhanh để phân biệt từng tiếng, không đều.",
            "subclinical": "- **ECG:** Cơn nhịp nhanh trên thất, phức bộ QRS thanh mảnh nhưng nhịp hoàn toàn không đều, xen kẽ các nhịp với hình thái WPW (rung nhĩ trên nền WPW). Tần số 180-210 l/p.",
            "question": "👉 Khoa cấp cứu: Rung nhĩ đáp ứng thất cực nhanh trên nền hội chứng WPW. Chống chỉ định dùng thuốc nào trong trường hợp này (VD: Digoxin, Verapamil)? Nên xử trí sốc điện hay Amiodarone?"
        },
        {
            "name": "Lương Lữ H", "age": 42, "sex": "Nữ", "job": "Nhân viên văn phòng", "specialty": "TIM MẠCH",
            "reason": "Sốt cao, rét run kèm khó thở và sưng khớp gối.",
            "history": "- Sốt vã mồ hôi về chiều 2 tuần nay (38.5 độ). Gần đây chán ăn sụt 3kg. Khó thở tăng dần khi nằm. Hôm qua xuất hiện đau buốt khớp gối phải.",
            "past_medical": "- Nhổ răng số 48 cách đây 3 tuần tại phòng khám tư nhưng không uống kháng sinh đủ liều.",
            "clinical": "**Sinh hiệu:** Nhiệt độ 39 độ C, Mạch 105 l/p, HA 110/60 mmHg.\n**Tim mạch:** Nghe có tiếng thổi tâm thu 4/6 ở mỏm tim lan nách, nghe như xé lụa. \n**Ngoại biên:** Xuất huyết dưới móng tay (Splinter hemorrhages), nốt Osler ngón tay.",
            "subclinical": "- **Cấy máu:** Dương tính với Streptococcus viridans.\n- **Siêu âm tim qua thành ngực:** Mảnh sùi 12x8 mm bám ở lá trước van 2 lá, di động mạnh, hở van 2 lá nặng.",
            "question": "👉 Viêm nội tâm mạc nhiễm khuẩn bán cấp biến chứng hở van 2 lá nặng. Lựa chọn phác đồ kháng sinh nào theo mức độ nhạy cảm và thời gian truyền tĩnh mạch là bao lâu?"
        },
        {
            "name": "Bùi Tấn C", "age": 68, "sex": "Nam", "job": "Hưu trí", "specialty": "TIM MẠCH",
            "reason": "Đau rách xé vùng lưng ngực, vã mồ hôi.",
            "history": "- Đột ngột đau dữ dội, cảm giác như xé rách từ trong lồng ngực lan xuyên ra giữa hai xương bả vai. Đáy mắt tối sầm.",
            "past_medical": "- Tăng HA mạn tính không kiểm soát (HA thường xuyên > 160). Hút thuốc lá 30 bao/năm.",
            "clinical": "**Sinh hiệu:** HA tay phải 180/100, HA tay trái 140/80. Mạch 90 l/p.\n**Mạch ngoại vi:** Bắt mạch quay hai tay không đều.",
            "subclinical": "- **X-quang:** Quai động mạch chủ giãn rộng lớn rãnh.\n- **CT Angiography lồng ngực:** Hình ảnh lóc tách động mạch chủ ngực Stanford tuýp B dài 12cm, lòng giả lớn hơn lòng thật.",
            "question": "👉 Lóc tách động mạch chủ tuýp B cấp tính. Ưu tiên kiểm soát huyết áp bằng truyền tĩnh mạch thuốc gì theo phác đồ? Mức huyết áp tâm thu mục tiêu trong giờ đầu là bao nhiêu?"
        },
        {
            "name": "Cam Hữu Đ", "age": 85, "sex": "Nam", "job": "Hưu trí", "specialty": "TIM MẠCH",
            "reason": "Phù to, báng bụng và tím tái toàn thân.",
            "history": "- Khó thở liên tục cả lúc nghỉ ngơi. Đi tiểu rất ít <400ml/ngày. Bụng chướng to dần.",
            "past_medical": "- Tâm phế mạn do COPD 15 năm.",
            "clinical": "**Sinh hiệu:** O2 87% khí trời. Tím môi và đầu chi.\n**Lâm sàng:** TM cổ nổi to, gan to độ 3 cứng, báng bụng mạn tính. Phù cứng hai chi dưới.",
            "subclinical": "- **Siêu âm tim:** Áp lực ĐM phổi (PAPs) 75 mmHg. Suy thất phải nặng.\n- **Khí máu:** PaO2 55, PaCO2 68 (Toan hô hấp mạn).",
            "question": "👉 Suy tim phải giai đoạn cuối (Tâm phế mạn) do COPD. Điều chỉnh oxy liệu pháp như thế nào để tránh ngưng thở? Có nên dùng chẹn beta giao cảm không?"
        },
        {
            "name": "Dương Kim L", "age": 25, "sex": "Nữ", "job": "Nhân viên viên PG", "specialty": "TIM MẠCH",
            "reason": "Đánh trống ngực, run tay, sụt cân và tức ngực nhẹ.",
            "history": "- Cảm giác tim đập rất nhanh hồi hộp như chực bay ra ngoài, tay rỉ mồ hôi. Sụt 4kg/tháng. Hay cấu gắt.",
            "past_medical": "- Gia đình mẹ có bướu cổ.",
            "clinical": "**Sinh hiệu:** Mạch 120 l/p đều, HA 130/70. Nhiệt đới 37.5 C.\n**Mắt & Cổ:** Mắt lồi nhẹ, bướu giáp lan tỏa độ II có âm thổi tâm thu tại tuyến giáp.",
            "subclinical": "- **Tuyến giáp:** TSH < 0.01 uU/ml, FT4 tăng gấp 3 lần.\n- **ECG:** Nhịp nhanh xoang 125 l/p.",
            "question": "👉 Biến chứng tim mạch do Basedow (Nhiễm độc giáp). Phác đồ kiểm soát nhịp tim ban đầu bằng Propranolol nên chỉ định với liều nào?"
        },
        {
            "name": "Đinh Bách V", "age": 58, "sex": "Nam", "job": "Doanh nhân", "specialty": "TIM MẠCH",
            "reason": "Khám mệt mỏi mạn tính, HA không hạ dù đã dùng 3 loại thuốc.",
            "history": "- Bệnh nhân than phiền nhức đầu vùng chẩm, mắt hay mờ. Đang uống Amlodipine, Valsartan, và Hydrochlorothiazide liều tối đa nhưng HA vẫn ở mức 160-170.",
            "past_medical": "- Tăng HA kháng trị đã 2 năm.",
            "clinical": "**Lâm sàng:** Nghe thấy tiếng thổi tâm thu rõ ở mạn sườn trái khi bệnh nhân nằm.",
            "subclinical": "- **Siêu âm Doppler mạch thận:** Hẹp 80% gốc động mạch thận bên trái.\n- **Thận:** Creatinin 130 umol/L.",
            "question": "👉 Tăng huyết áp thứ phát do hẹp động mạch thận (THA kháng trị). Có nên chống chỉ định hoặc dừng Valsartan (thuốc ức chế thụ thể) trong trường hợp này không?"
        }
    ],

    "🫁 Hô hấp": [
        {
            "name": "Nguyên Khang V", "age": 65, "sex": "Nam", "job": "Bảo vệ", "specialty": "HÔ HẤP",
            "reason": "Khó thở dữ dội, khạc đờm mủ đục vàng.",
            "history": "- Ho mạn tính nhiều năm, đờm trắng. 3 ngày nay ho tăng, đờm chuyển màu vàng xanh đặc, khó thở rút lõm lồng ngực không thể nằm.",
            "past_medical": "- Hút thuốc lá 40 gói/năm. Đã chẩn đoán COPD 5 năm trước, thỉnh thoảng xịt Ventolin.",
            "clinical": "**Sinh hiệu:** Mạch 115 l/p, HA 140/85, SpO2 86% khí trời.\n**Hệ Hô hấp:** Lồng ngực hình thùng. Phổi gáy rì rào phế nang mờ nhạt, ran rít ran ngáy vang dội.",
            "subclinical": "- **X-quang ngực:** Hình ảnh phổi sáng, vòm hoành dẹt.\n- **Khí máu động mạch:** pH 7.28, PaCO2 58 mmHg (Toan hô hấp mất bù).",
            "question": "👉 Đợt cấp COPD mức độ nặng. Xin đề xuất phác đồ thở máy không xâm nhập (BiPAP) kết hợp corticoid toàn thân và kháng sinh hô hấp."
        },
        {
            "name": "Võ Thị Na", "age": 28, "sex": "Nữ", "job": "Giáo viên mầm non", "specialty": "HÔ HẤP",
            "reason": "Lên cơn ho rũ rượi, thở rít tái nhợt vì bụi phấn.",
            "history": "- Đang dạy học lau bảng phấn thì xuất hiện ho rũ rượi, khó thở ra rõ rệt, ngực có tiếng rít như tiếng cò súng phô vang trong lớp.",
            "past_medical": "- Hen phế quản dị ứng phấn hoa từ năm 12 tuổi, bỏ trị.",
            "clinical": "**Sinh hiệu:** Mạch 110, SpO2 91%. Có kéo cơ thế hô hấp phụ mạnh.\n**Phổi:** Rì rào phế nang giảm, ran rít ran ngáy khắp hai phế trường.",
            "subclinical": "- **Đỉnh lưu lượng:** Giảm xuống còn 40% giá trị dự đoán.",
            "question": "👉 Cơn hen phế quản cấp tính mức độ nặng. Phác đồ sử dụng khí dung chẹn beta (Salbutamol) và Corticoid liều cao tiêm tĩnh mạch như thế nào?"
        },
        {
            "name": "Phùng Viết H", "age": 45, "sex": "Nam", "job": "Xây dựng", "specialty": "HÔ HẤP",
            "reason": "Sốt cao 39 độ, đau ngực trái kiểu màng phổi khi hít sâu.",
            "history": "- Cách vào viện 4 ngày chán ăn, gai rét. 2 ngày nay sốt cao, ho khạc đờm màu rỉ sắt, đau nhức tức ngực bên trái mỗi khi cố hít sâu vào.",
            "past_medical": "- Nghiện rượu mạn tính.",
            "clinical": "**Sinh hiệu:** Nhiệt 39.5, Mạch 100 l/p, HA 110/70.\n**Hệ Hô hấp:** Hội chứng đông đặc đáy phổi trái (RRPN giảm, gõ đục, rung thanh tăng). Có ran nổ rõ mồn một.",
            "subclinical": "- **X-quang ngực:** Mờ đồng đều phân thùy dưới phổi trái, có hình ảnh phế quản chứa khí (air bronchogram).\n- **Bạch cầu:** 18.000/mm3 (Neu 85%).",
            "question": "👉 Viêm phổi mắc phải cộng đồng (CAP) trên nền nghiện rượu (nghi do phế cầu hoặc Klebsiella). Lựa chọn Kháng sinh kinh nghiệm tiêm tĩnh mạch đầu tiên là gì?"
        },
        {
            "name": "Đoàn Tấn L", "age": 70, "sex": "Nam", "job": "Thợ hàn", "specialty": "HÔ HẤP",
            "reason": "Ho ra máu tươi 200ml, sụt cân 5kg.",
            "history": "- Ho húng hắng 3 tháng nay, người mệt mỏi sụt cân. Sáng nay tự nhiên ho ra một búng máu tươi có lẫn vài cục máu đông.",
            "past_medical": "- Hút thuốc 50 gói/năm. Không rõ tiếp xúc bệnh lao.",
            "clinical": "**Toàn thân:** Gầy rộc, ngón tay dùi trống.\n**Phổi:** Hội chứng ba giảm 1/3 trên phổi phải.",
            "subclinical": "- **CT Scanner lồng ngực:** Khối u thùy trên phổi phải kích thước 4x5cm, bờ tua gai xâm lấn màng phổi, kèm tràn dịch trung bình. Có hạch rốn phổi.",
            "question": "👉 Ho ra máu mức độ vừa do K phổi thùy trên phải. Chỉ định nội soi phế quản cầm máu và làm sinh thiết có phù hợp lúc này không?"
        },
        {
            "name": "Mã Văn T", "age": 32, "sex": "Nam", "job": "Giao hàng", "specialty": "HÔ HẤP",
            "reason": "Sốt nhẹ về chiều, ho đờm và đổ mồ hôi trộm.",
            "history": "- Ho kéo dài 4 tuần không dứt. Mệt mỏi, sốt về chiều (37.5-38), đổ mồ hôi ướt áo lúc nửa đêm.",
            "past_medical": "- Bạn cùng phòng trọ mới được chẩn đoán Lao AFB dương tính.",
            "clinical": "**Hệ Hô hấp:** Gõ đục nhẹ, ran nổ khu trú vùng đỉnh phổi trái.",
            "subclinical": "- **X-quang ngực:** Tổn thương thâm nhiễm đám gõ nhẹ và tạo hang nhỏ 2cm vùng đỉnh phổi trái.\n- **AFB đờm 2 mẫu:** Dương tính (2+).",
            "question": "👉 Bệnh Lao phổi AFB (+). Xin nêu rõ phác đồ điều trị lao Mới (Phác đồ 6 tháng theo chương trình Chống lao QG) gồm các loại thuốc gì?"
        },
        {
            "name": "Chu Hải Đ", "age": 55, "sex": "Nam", "job": "Lái xe", "specialty": "HÔ HẤP",
            "reason": "Ngủ ngáy to, buồn ngủ gật gà gật gù ban ngày.",
            "history": "- Vợ phàn nàn bệnh nhân ngáy rất to, thi thoảng nín thở lúc ngủ khiến vợ hoảng sợ phải vỗ dậy. Ban ngày lái xe dễ buồn ngủ thiu thiu, mất tập trung.",
            "past_medical": "- Béo phì BMI 31, Tăng HA vòng bụng 105cm.",
            "clinical": "**Lâm sàng:** Cổ bành to, họng hẹp (Mallampati đo độ 3), amidan quá phát.",
            "subclinical": "- **Đo đa ký giấc ngủ (Polysomnography):** Chỉ số AHI (Apnea-Hypopnea Index) là 45 lần/giờ (Mức độ rất nặng).",
            "question": "👉 Hội chứng Ngưng thở khi ngủ do tắc nghẽn (OSA) mức độ nặng. Bệnh nhân này có chỉ định thở máy CPAP ban đêm như thế nào?"
        },
        {
            "name": "Trịnh Mỹ A", "age": 22, "sex": "Nữ", "job": "Nội trợ", "specialty": "HÔ HẤP",
            "reason": "Đau nhói ngực trái buốt như dao đâm, khó thở sau rặn táo bón.",
            "history": "- Đang ngồi làm gắng sức rặn toilet thì nghe 'kịch' một tiếng trong ngực. Giật bắn đau xé ngực trái, thở rất nông vì hít vào là đau.",
            "past_medical": "- Hội chứng Marfan (Người cao gầy lêu nghêu 1m75, 45kg).",
            "clinical": "**Phổi:** Tràn khí màng phổi tụt (Hội chứng 3 giảm do khí chèn). Gõ vang như trống 1/2 trên phổi trái.",
            "subclinical": "- **X-quang ngực đứng:** Tràn khí màng phổi trái mức độ nhiều, đẩy lệch trung thất sang phải.",
            "question": "👉 Tràn khí màng phổi tự phát nguyên phát do vỡ bóng khí ngực. Vị trí chọc hút kim và chỉ định mở màng phổi dẫn lưu kín?"
        },
        {
            "name": "Ông Khắc C", "age": 60, "sex": "Nam", "job": "Về hưu", "specialty": "HÔ HẤP",
            "reason": "Khó thở dữ dội, tức ngực sượng sùng sau ca mổ thay khớp háng.",
            "history": "- Ngày thứ 7 sau mổ thay khớp háng phải (vẫn nằm bất động nhiều), đột ngột tím tái, khó thở cấp bách, mạch đập nhanh, vã mồ hôi.",
            "past_medical": "- Tăng HA, Đái tháo đường. Giãn TM chi dưới.",
            "clinical": "**Sinh hiệu:** Mạch 125 l/p, HA tụt chậm 90/60, SpO2 88%.",
            "subclinical": "- **D-Dimer:** Tăng > 5000 ng/ml.\n- **CT ĐM Phổi (CTPA):** Huyết khối tắc nghẽn nhánh lớn động mạch phổi thùy dưới bên phải.\n- **Siêu âm tĩnh mạch sâu:** Huyết khối DVT tĩnh mạch khoeo phải.",
            "question": "👉 Nhồi máu phổi (Thuyên tắc phổi) cấp tính trên nền huyết khối tĩnh mạch sâu. Chỉ định thuốc tiêu sợi huyết có an toàn trên bệnh nhân vừa mổ 7 ngày không?"
        },
        {
            "name": "Bùi Mai T", "age": 42, "sex": "Nữ", "job": "Nông dân", "specialty": "HÔ HẤP",
            "reason": "Tức nặng hạ sườn phải, ho khan, sốt nhẹ.",
            "history": "- Mẩn ngứa nhiều ngày. Sau đó sốt nhẹ, ho khan túc tắc, cảm giác như có cục cứng chèn ép mạng sườn phải gây khó thở hụt hơi.",
            "past_medical": "- Thường xuyên ăn gỏi cá sống, rau muống chẻ sống.",
            "clinical": "**Sinh hiệu:** Mạch 90 l/p. Nhiệt độ 37.8.\n**Lâm sàng:** Hội chứng 3 giảm đáy phổi phải (nghĩ do tràn dịch). Gan to 3cm, ấn đau.",
            "subclinical": "- **Siêu âm:** Tràn dịch màng phổi phải lượng vừa, ổ áp xe gan bờ không đều.\n- **Xét nghiệm huyết thanh:** Dương tính Sán lá gan lớn (Fasciola gigantica). Bạch cầu ái toan tăng 25%.",
            "question": "👉 Tràn dịch màng phổi thứ phát do áp xe sán lá gan vỡ hở. Vui lòng cho phác đồ diệt sán bằng Triclabendazole."
        },
        {
            "name": "Lê Hải H", "age": 30, "sex": "Nam", "job": "Lính cứu hỏa", "specialty": "HÔ HẤP",
            "reason": "Ho kịch phát đỏ mặt, bỏng rát phế quản do hít khói.",
            "history": "- Kẹt trong phòng chữa cháy nhà xưởng nhựa 10 phút. Hít phải lượng lớn khói đen. Giọng nói khàn rọt, ho sặc sụa, dãi đen nhẻm.",
            "past_medical": "- Khỏe mạnh.",
            "clinical": "**Toàn thân:** Lông mi, lông mũi cháy sém. Bỏng nhám vùng mặt. Niêm mạc mũi họng đen than.\n**Phổi:** Rì rào phế nang thô, nhiều ran rít co thắt.",
            "subclinical": "- **Khí máu (ABG):** COHb lên tới 25%. \n- **Nội soi phế quản:** Niêm mạc phù nề, xuất huyết nhiều hạt bụi than bám.",
            "question": "👉 Bỏng đường hô hấp do ngạt khói có ngộ độc khí CO. Tiên lượng đặt nội khí quản chủ động sớm và lập phác đồ Oxy cao áp (Hyperbaric oxygen)?"
        }
    ],

    "🔬 Nội tiết": [
        {
            "name": "Trần Ngọc T", "age": 58, "sex": "Nam", "job": "Viên chức", "specialty": "NỘI TIẾT",
            "reason": "Uống nhiều, tiểu nhiều, mệt mỏi rã rời sụt 6kg/tháng.",
            "history": "- Tiểu đêm 4-5 lần, khát nước liên tục uống 3-4 lít ngày. Mắt nhìn mờ, sụt 6kg dù ăn uống bình thường. Hay kiến bò đầu ngón chân.",
            "past_medical": "- Tiền ĐTĐ 3 năm không kiêng cữ.",
            "clinical": "**Toàn thân:** Thể trạng béo (BMI 26), mỡ bụng nhiều. Da niêm mạc khô.\n**Thần kinh:** Giảm cảm giác rung âm thoa bàn chân 2 bên.",
            "subclinical": "- **Đường huyết đói (FPG):** 11.5 mmol/L.\n- **HbA1c:** 9.8%.\n- **Nước tiểu:** Tiêu Protenin vi lượng (Microalbumin niệu) dương tính.",
            "question": "👉 Đái tháo đường type 2 mới chẩn đoán, đường huyết rất cao kèm biến chứng thần kinh/thận sớm. Phác đồ khởi trị: Phối hợp ngay Insulin nền hay dùng 2 thuốc viên uống?"
        },
        {
            "name": "Bùi Tuyết G", "age": 60, "sex": "Nữ", "job": "Nông dân", "specialty": "NỘI TIẾT",
            "reason": "Hôn mê gọi hỏi không biết, thở ngáp cá, lơ mơ.",
            "history": "- Nằm ốm sốt nôn mửa ăn uống kém 3 ngày. Sáng nay người nhà gọi không dậy, hơi thở mùi táo úng rực rỡ.",
            "past_medical": "- ĐTĐ type 1 (từ hồi 30t) chích Insulin hỗn hợp 2 lần/ngày. 3 ngày nay sốt bỏ ăn nên tự ngưng tiêm thuốc.",
            "clinical": "**Sinh hiệu:** Mạch 125 l/p yếu, HA 85/50. Nhịp thở Kussmaul sâu và cực kì nhanh (35 l/p).\n**Toàn thân:** Cơ thể khô hạn nặng, véo da lưu lâu.",
            "subclinical": "- **Đường huyết mao mạch:** HI (>33.3 mmol/L).\n- **Khí máu động mạch:** pH = 7.10, HCO3- = 10 (Toan chuyển hóa nặng).\n- **Nước tiểu:** Keton (+++). K+ máu 3.5.",
            "question": "👉 Nhiễm toan Ceton do đái tháo đường (DKA) nặng trên ĐTĐ Type 1 bỏ thuốc. Phác đồ truyền dịch Natri clorid 0.9% và phác đồ Insulin bơm tiêm điện chuẩn?"
        },
        {
            "name": "Hà Vĩnh M", "age": 75, "sex": "Nam", "job": "Hưu trí", "specialty": "NỘI TIẾT",
            "reason": "Lú lẫn, yếu liệt nửa người nghi đột quỵ.",
            "history": "- Bệnh nhân ĐTĐ tuýp 2 uống Gliclazide buổi sáng nhưng sau đó bỏ bữa ăn sáng do cãi nhau với vợ. Trưa nay vã mồ hôi đầm đìa, tay chân run lẩy bẩy rồi ngã khuỵu, mất ý thức.",
            "past_medical": "- ĐTĐ tuýp 2 đang dùng Sulfonylurea liều trung bình.",
            "clinical": "**Sinh hiệu:** Mạch 110, HA 130/80.\n**Thần kinh:** Trạng thái lú lẫn kích động mạnh. Không liệt khu trú thực thể.",
            "subclinical": "- **Đường dúng ngón tay (Test nhanh):** 1.8 mmol/L.",
            "question": "👉 Hôn mê do Hạ đường huyết do dùng nhóm Sulfonylurea bỏ bữa ăn. Ưu tiên cấp cứu tiêm tĩnh mạch thứ gì ngay lập tức tại phòng cấp cứu?"
        },
        {
            "name": "Nguyễn Hoàng P", "age": 40, "sex": "Nữ", "job": "Nội trợ", "specialty": "NỘI TIẾT",
            "reason": "Tăng cân không kiểm soát, rạn da bụng ửng đỏ, teo cơ chân tay.",
            "history": "- Tăng 15kg trong 6 tháng. Mặt phù to đỏ rực như mặt trăng, bụng mỡ dày cộm nhưng chân tay thì teo nhỏ lại lỏng lẻo. Lông tơ mọc mép rậm rì.",
            "past_medical": "- Đau khớp gối mạn hay ra tiệm thuốc tây mua 'thuốc bọc nhộng' uống 5 năm qua.",
            "clinical": "**Toàn thân:** Hội chứng Cushing lâm sàng điển hình (Beo trung tâm, rạn da tím vùng bẹn/bụng).\n**Sinh hiệu:** HA 160/95 mmHg.",
            "subclinical": "- **Cortisol máu 8h sáng:** Dưới ngưỡng (< 50 nmol/L). Tuyến thượng thận teo trên Siêu âm.",
            "question": "👉 Hội chứng Cushing do thuốc (Iatrogenic Cushing) suy tuyến thượng thận thứ phát trầm trọng. Các bước cai nghiện Corticoid từ từ để tránh suy thượng thận cấp?"
        },
        {
            "name": "Phạm Nữ T", "age": 35, "sex": "Nữ", "job": "Giáo viên", "specialty": "NỘI TIẾT",
            "reason": "Run tay, trống ngực, lồi mắt, sụt cân nhiều.",
            "history": "- Cổ to dần, tim đập thình thịch 110-120 cả lúc ngủ. Ăn rất được nhưng sụt 8kg trong 2 tháng. Mắt trái cảm giác trợn trạo mỏi.",
            "past_medical": "- Khỏe mạnh.",
            "clinical": "**Tuyến giáp:** Bướu giáp lan tỏa, cứng chắc, nghe âm thổi tâm thu cường độ 3/6.\n**Thần kinh:** Run mao biên hai tay.",
            "subclinical": "- **TSH:** < 0.005 uU/ml (giảm sâu). **FT4:** Tăng vọt gấp 4 lần.\n- **TRAb:** Dương tính rất cao.",
            "question": "👉 Cường giáp Basedow (Bệnh Graves). Thuốc kháng giáp tổng hợp (PTU hay Methimazole) được khuyến cáo lựa chọn đầu tay theo phác đồ?"
        },
        {
            "name": "Lê Phước S", "age": 50, "sex": "Nam", "job": "Bảo vệ", "specialty": "NỘI TIẾT",
            "reason": "Mệt rũ rượi buồn ngủ cả ngày, sợ lạnh, tăng cân.",
            "history": "- Gần đây phản ứng rất chậm chạp, nói lờ đờ, da khô khốc nhợt nhạt và lông mày rụng ở 1/3 ngoài. Cực kỳ sợ lạnh, hay mác táo bón.",
            "past_medical": "- Cắt toàn bộ tuyến giáp do K Giáp 2 năm trước.",
            "clinical": "**Toàn thân:** Phù niêm (myxedema) vùng mặt, bắp chân lõm không đàn hồi.\n**Sinh hiệu:** Nhịp tim chậm 55 l/p.",
            "subclinical": "- **TSH:** > 100 uU/ml. **FT4:** Rất thấp dưới ngưỡng máy đo.",
            "question": "👉 Suy giáp do phẫu thuật cắt giáp bỏ điều trị hormone. Liều bổ sung Levothyroxine khởi đầu phụ thuộc vào yếu tố nào (tuổi, bệnh lý tim mạch đi kèm)?"
        },
        {
            "name": "Đặng Thị K", "age": 45, "sex": "Nữ", "job": "Nội trợ", "specialty": "NỘI TIẾT",
            "reason": "Đau mỏi xương khớp, siêu âm có sỏi thận tái phát.",
            "history": "- Thỉnh thoảng đi tiểu ra cặn sỏi nhỏ. Tay chân nhức mỏi buồn bực trong xương tủy.",
            "past_medical": "- Mổ lấy sỏi niệu quản 3 lần trong 5 năm. Viêm loét dạ dày.",
            "clinical": "**Lâm sàng:** Ấn các điểm xương đau nhẹ, cổ không thấy khối u rõ trên da.",
            "subclinical": "- **Calcium máu:** Tăng cao 3.1 mmol/L. \n- **PTH (Parathyroid Hormone):** Tăng vọt 250 pg/ml.\n- **Siêu âm cổ:** U tuyến cận giáp nhỏ 1.5cm sau thùy trái tuyến giáp.",
            "question": "👉 Cường cận giáp nguyên phát do U tuyến cận giáp. Có nên chống chỉ định dùng thuốc Lợi tiểu Thiazide ở bệnh nhân này không?"
        },
        {
            "name": "Vũ Anh D", "age": 25, "sex": "Nam", "job": "Sinh viên", "specialty": "NỘI TIẾT",
            "reason": "Khát nước cháy họng, đi tiểu 10 lít mỗi ngày.",
            "history": "- Luôn cầm kè chai nước lọc khổng lồ. 20 phút đi tè một lần, nước tiểu trong vắt như nước suối. Khát không chịu nổi nếu không uống.",
            "past_medical": "- Chấn thương sọ não do tai nạn giao thông 1 tháng trước (nứt khe bướm).",
            "clinical": "**Toàn thân:** Khô môi miệng, giảm độ đàn hồi da.",
            "subclinical": "- **Đường huyết đói:** Bình thường 5.2.\n- **Tỷ trọng nước tiểu:** 1.002 (Rất thấp).\n- **Na+ máu (Sodium):** Chỉ số cao 152 mmol/L.",
            "question": "👉 Đái tháo nhạt trung ương thứ phát sau chấn thương sọ não. Làm nghiệm pháp nhịn khát và test Desmopressin để chẩn đoán xác định thế nào?"
        },
        {
            "name": "Lâm Quốc T", "age": 60, "sex": "Nam", "job": "Nông dân", "specialty": "NỘI TIẾT",
            "reason": "Sưng nóng đỏ rực ngón chân cái bên phải dữ dội.",
            "history": "- Nửa đêm sau bữa tiệc thịt chó mắm tôm, ngón chân cái chân phải bỏng rát, đỏ chói, bóng lộn, đau kịch liệt không dám đắp mùng chạm vào.",
            "past_medical": "- Tăng HA mạn, thường dùng uống bia mỗi chiều.",
            "clinical": "**Khớp:** Viêm khớp bàn ngón chân cái T cấp tính điển hình. Sờ ấm nóng, sung huyết đỏ tươi.",
            "subclinical": "- **Axit Uric máu:** 680 umol/L.\n- **X-quang:** Có đám mờ phù nề mô mềm, chưa khuyết xương.",
            "question": "👉 Cơn Gout cấp tính điền hình. Trong lúc đau cấp, có nên kê đờn Allopurinol luôn không hay chỉ nên dùng Colchicine + giảm đau NSAIDs?"
        },
        {
            "name": "Đỗ Hà P", "age": 30, "sex": "Nữ", "job": "IT", "specialty": "NỘI TIẾT",
            "reason": "Huyết áp tăng cực điểm thành cơn 200/120 kèm hồi hộp 120 nhịp.",
            "history": "- Đột ngột phát hỏa, HA vọt lên 200, tay chân run lẩy bẩy, bốc hỏa, vã mồ hôi đầm đìa kéo dài 20 phút rồi tự hạ.",
            "past_medical": "- Tình trạng này xuất hiện hàng tuần, đo siêu âm bụng rờ thấy gan nhiễm mỡ.",
            "clinical": "**Khám ngoài cơn:** HA bình thường 120/80.\n**Khám trong cơn:** Mạch 130, HA 210/115.",
            "subclinical": "- **Catecholamine nước tiểu 24h & Metanephrine:** Tăng gấp 5 lần so với cực đại bình thường.\n- **CT Bụng:** Khối u thận thượng thận P 5cm, ngậm thuốc cản quang mạnh.",
            "question": "👉 U tủy thượng thận (Pheochromocytoma). Phác đồ sử dụng thuốc ức chế Alpha blocker (Prazosin) phải dùng trước khi sử dụng Beta-blocker đúng không?"
        }
    ],

    "🦷 Răng Hàm Mặt": [
        {
            "name": "Trần Văn T", "age": 28, "sex": "Nam", "job": "Kỹ sư Cầu Đường", "specialty": "RĂNG HÀM MẶT",
            "reason": "Đau nhức vùng góc hàm MẶT phải lan lên mang tai, há miệng hạn chế.",
            "history": "- Đau âm ỉ 3 ngày nay, tăng dần cản trở nuốt. Nay bắt đầu sốt 37.8 độ, hơi thở hôi lợm đắng miệng.",
            "past_medical": "- Nhổ răng 38 năm ngoái. Không dị ứng kháng sinh.",
            "clinical": "**Tại chỗ:** Vùng lợi trùm bọc che chân răng 48 sưng viêm đỏ phổng, rỉ mủ màu vàng đục khi ấn nhẹ. Răng 48 đâm kẹt vướng mép.\n**Hệ thống:** Hạch góc hàm phải lớn bằng hạt nhãn sờ di động đau.",
            "subclinical": "- **X-quang Panorama:** Khoảng sáng vùng 48 không rõ, răng mọc lệch gần góc 90 độ, đâm thẳng lưng răng 47 gây tiêu xương ngách nhỏ.",
            "question": "👉 Viêm lợi trùm biến chứng áp xe cấp tính do răng khôn 48 mọc lệch. Phác đồ KS kháng kỵ khí cơ bản và thời điểm Vàng chỉ định nhổ răng theo BYT?"
        },
        {
            "name": "Lý Thị Trinh", "age": 35, "sex": "Nữ", "job": "Kế toán trưởng", "specialty": "RĂNG HÀM MẶT",
            "reason": "Răng số 16 cắn buốt dữ dội, đau giật nhói lên thái dương, thức trắng đêm.",
            "history": "- Răng ê ẩm nhiều tháng nay, nhưng kịch phát đêm qua đau buốt xé tai kéo dài từng đợt 30 phút, ngậm nước đá vào đau điếng dội lên não.",
            "past_medical": "- Răng 16 đã trám mẻ hỗn hống amalgam tự rụng lâu ngày.",
            "clinical": "**Khám nha:** Răng 16 bục lỗ sâu to mặt nhai ngót gần đụng tủy, thám trâm rạch đáy buốt chói chết người. Gõ dọc đau chói, gõ ngang không đau. Lợi bình thường quanh chóp.",
            "subclinical": "- **X-quang Chóp:** Vùng thấu quang dải rộng ăn cụt ngà sát buồng tủy gốc răng 16. Chân răng dây chằng nguyên vẹn, gờ xương cứng chắc.",
            "question": "👉 Viêm tủy cấp không hồi phục răng 16. Kỹ thuật Gây tê, lấy tủy sống ngay tức thì (Pulpectomy) và quy trình nong dũa bơm rửa ống tủy?"
        },
        {
            "name": "Nguyễn Minh Khang", "age": 62, "sex": "Nam", "job": "Nhà văn", "specialty": "RĂNG HÀM MẶT",
            "reason": "Răng cửa hai hàm lung lay, mủ chảy từ chân răng khi đánh răng.",
            "history": "- Tình trạng răng miệng tệ nhiều năm, răng cửa thụt lút có thể tự đu gãy dứt được. Răng ê liên tục khi nhai đồ sượng.",
            "past_medical": "- Đái tháo đường type 2 đường máu thường lấp lửng biên độ cao (Kém kiểm soát). Hút thuốc 1 gói/ngày.",
            "clinical": "**Tại chỗ:** Vôi răng nguyên mảng khổng lồ đóng cục cổ răng. Túi nha chu viêm nha chu nông 7-8mm, rỉ mủ. Răng cửa dưới (31, 41) lung lay độ III bật khỏi ổ. Lợi tụt lộ tận chân xi-măng.",
            "subclinical": "- **X-quang:** Tiêu xương ổ lởm chởm mức 2/3 phần chóp dọc toàn hàm.",
            "question": "👉 Viêm nha chu mạn lan tỏa nặng do biến chứng Tiểu đường và Thuốc lá. Quy trình xử lý Nạo túi nha chu, lật vạt và giữ chỉ định Rút bỏ các răng lung lay tuyệt vọng?"
        },
        {
            "name": "Đặng Bảo Châu", "age": 8, "sex": "Nữ", "job": "Học sinh", "specialty": "RĂNG HÀM MẶT - TRẺ EM",
            "reason": "Sưng nề to biến dạng gò má má phải, góc hàm sưng tím, kèm sốt li bì.",
            "history": "- Em bé kêu nhức răng sữa số 84 vài tuần nhưng mẹ mua thuốc giảm đau cho ngậm bong ra. Hôm nay sưng phồng má phải, nheo mắt không nổi sưng to, sốt đừ người, bỏ ăn.",
            "past_medical": "- Men răng xấu sâu rải rác. Thể tràng gầy gò.",
            "clinical": "**Toàn thân:** Nhiệt 39.2 độ.\n**Tại chỗ:** Khối abces sờ biến dạng má phải lớn, cảm giác sờ phập phều căng tức.\n**Nội nha:** Răng 84 vỡ thân răng to hoác bốc mùi thối mủ thúi.",
            "subclinical": "- **BC máu:** Lên cao mức Bạch cầu 16k.\n- **XQ:** Viêm quanh chóp 84 phá ổ mủ lớn có nguy cơ lây túi hoại lang mầm răng 44 phía dưới.",
            "question": "👉 Viêm tấy mô liên kết – Áp xe tiền đình lây chóp răng sữa 84. Chống chỉ định hay có chỉ định Nhổ Răng 84 Giải Áp trong giai đoạn cấp này?"
        },
        {
            "name": "Vũ Huy Hoàng", "age": 42, "sex": "Nam", "job": "Shipper", "specialty": "RĂNG HÀM MẶT - CHẤN THƯƠNG",
            "reason": "Đập mặt vỉa hè té xe đứt rách môi môi dưới, khớp cắn hở chênh vênh.",
            "history": "- Tai nạn va quệt bầm mặt, đập trực diện má trái và cằm xuống đường. Băng gạc dính bết rách môi chảy máu.",
            "past_medical": "- Khỏe, không xỉn rượu.",
            "clinical": "**Tại chỗ:** Lệch cằm sang phải. Rách niêm mạc ngách lợi kẽ môi trái. Sờ có nấc ấn trượt vùng khe răng hàm 34-35 (bậc thang xương hụt hẫng). Há miệng đụng hàm kẹt nhẹ.",
            "subclinical": "- **X-quang Cone Beam CT (CBCT):** Gãy xương hàm dưới đơn thuần băng qua vùng răng 35, đường gãy xé nhọn. Cổ lồi cầu hai bên nguyên vẹn.",
            "question": "👉 Gãy xương hàm dưới thể góc ngầm hàm trái qua răng. Phương pháp phẫu thuật Cố định Kẹp Nẹp vít (Osteosynthesis plate) chỉ định khi nào?"
        },
        {
            "name": "Lưu Thanh Xuân", "age": 55, "sex": "Nữ", "job": "Buôn bán", "specialty": "RĂNG HÀM MẶT",
            "reason": "Hạt mụn đỏ cứng ngay dưới lưỡi, ăn hay bị vướng cộm đau đau.",
            "history": "- Khám vô tình nhột miệng thấy 1 cục thịt dư đỏ đục lừ sần sùi chai dưới hàm phải rìa lưỡi. 2 tháng nay to lên nhanh cỡ hạt lạc không đau, chạm vào chảy máu mủn.",
            "past_medical": "- Mang hàm giả tháo lắp 10 năm nay bị lỏng trượt đụng hay cọ vào niêm mạc lưỡi.",
            "clinical": "**Góc hàm:** Xuất hiện hạch nhỏ 1 cm dưới cằm. Vết loét chai sần 2cmx2cm bờ nham nhở cứng không đau tại bờ rìa hông lưỡi trái.",
            "subclinical": "- **Sinh thiết (Biopsy) cắm mẫu:** Chẩn đoán mô bệnh học - Ung thư Biểu Mô Tế Bào Vảy (SCC - Squamous Cell Carcinoma) biệt hóa vừa.",
            "question": "👉 Theo dõi Ung thư lưỡi (SCC) giai đoạn II. Quy trình hội chẩn ung bướu phẫu thuật cắt bán phần lưỡi và nạo hạch cổ sinh thiết như thế nào?"
        },
        {
            "name": "Huỳnh Tấn Phước", "age": 12, "sex": "Nam", "job": "Học sinh", "specialty": "RĂNG HÀM MẶT - CHỈNH NHA",
            "reason": "Răng hô đưa ra ngoài vẩu móm khó khép môi.",
            "history": "- Cha mẹ đưa đến khám vì tình trạng răng cháu vâu chìa lên không ngậm nổi môi mím, hay lỡ cắn mẻ răng và trêu ghẹo hô.",
            "past_medical": "- Có thói quen mút ngón tay hồi lên 9 tuổi.",
            "clinical": "**Ngoài mặt:** Nhìn nghiêng nét lồi cao vểnh. Môi trên hớt.\n**Trong mô:** Sai khớp cắn Hạng II Division 1 (Overjet tăng cực độ 10mm, răng cửa hất chìa gập hẹp cung hàm hàm trên).",
            "subclinical": "- **Phân tích phim Cephalometric:** Góc SNA 85 độ (Xương hàm trên nhô), SNB 76 độ (Xương hàm dưới lùi).",
            "question": "👉 Sai khớp cắn Hạng II do Xương. Phương án can thiệp chặn Chỉnh nha tăng trưởng cụ thể dùng khí cụ Twin-Block/ Headgear ở độ tuổi vàng này?"
        },
        {
            "name": "Bác Nông D", "age": 70, "sex": "Nam", "job": "Hưu trí", "specialty": "RĂNG HÀM MẶT - PHỤC HÌNH",
            "reason": "Mất hết sạch răng toàn hàm móm mém, nhai nhão niêm mạc, đau dạ dày.",
            "history": "- Bác mất sạch sành sanh răng hàm 4 năm nay, đeo hàm giả nhựa Acrilic lỏng quéo nhai cấn nướu cắn lưỡi xót xáy bầm mâm nướu. Ăn cơm cháo lỏng là chính mệt mỏi.",
            "past_medical": "- Huyết áp kiểm soát tốt. Tim mạch ổn định.",
            "clinical": "**Tại chỗ:** Mất toàn bộ 32 chóp răng. Tiêu tụt xương nghiêm trọng, sống hàm trên lép xẹp, hàm dưới hẹp như dao lở mỏng tanh. Niêm mạc phủ sung huyết xám sạm.",
            "subclinical": "- **Phim CT 3D:** Khối lượng xương mặt ngoài cực mỏng, chiều cao ngách xương hàm dưới chỉ 10mm giáp dây thần kinh răng dưới.",
            "question": "👉 Phục hình tháo lắp toàn hàm độ bám kém trụ xương tụt. Có chỉ định cắm Cấy ghép xương nhân tạo Implant All-on-4 đính trụ hàm hay không?"
        },
        {
            "name": "Phương Thùy G", "age": 22, "sex": "Nữ", "job": "Nhân viên BĐS", "specialty": "RĂNG HÀM MẶT",
            "reason": "Tẩy rát xót kinh khủng nướu tụt do dán răng sứ Ceramic tự chọn mạng.",
            "history": "- Tự đi tiệm Spa cỏ đắp phủ Ceramic 20 cái răng kim cương phong phủy đắp mù. 2 tháng sau máu hôi rình mủ chảy viền mép lợi ứa đau dữ.",
            "past_medical": "- Răng cũ vàng nhẹ khỏe mạnh.",
            "clinical": "**Tại nơi bị:** Viền nướu bờ viêm đỏ tực, đường hoàn tất nướu lòi cục Cement bọc dính thành mảng đè lên sinh học nướu (Vi phạm khoảng Sinh Học). Lợi nướu rỉ máu túi mủ ngứa.",
            "subclinical": "- **XQ:** Tiêu bờ mào xương kẽ răng cửa trên. Không hư tủy thấu.",
            "question": "👉 Viêm quanh răng hoại tử do phục hình dỏm hỏng mép vi phạm khoảng sinh học. Tiến trình tháo gỡ toàn bộ răng sứ viêm và ghép vạt lợi có khả thi?"
        },
        {
            "name": "Tôn Thất B", "age": 45, "sex": "Nam", "job": "Diễn viên", "specialty": "RĂNG HÀM MẶT",
            "reason": "Phát hiện Cục nang lớn ngầm xương hàm trên đi tình cờ nhổ răng.",
            "history": "- Răng số 12 hàm trên sâu tủy đã chữa mủ chóp từ 10 năm trước đóng chốt nấm, nay xưng lợi nhẹ không đau. Chụp nhổ răng thừa thì phát hiện.",
            "past_medical": "- Không đau đớn, thỉnh thoảng sưng nang ngách xẹp liền.",
            "clinical": "**Tại chỗ:** Cản trở tăm vùng phồng lồi đáy ngách hành lang 12-13. Bóp vào rộp như bóng nhựa (Ping-pong).",
            "subclinical": "- **XQ Panorama & CT:** Hình Oval vòng thấu quang cực lớn lấn nang kích thước 3x3 cm bao mút đầu chóp chân răng 12, phá vỡ vỏ xương mặt ngoài làm tiêu chân 13-11 cận kề ngậm nang.",
            "question": "👉 Nang chân răng (Nang do răng/Radicular Cyst) nhiễm trùng khổng lồ. Quy trình phẫu thuật cắt rộng bóc nang (Enucleation) và nhồi cốt ghép xương?"
        }
    ]
}

# ── Danh sách nhóm theo thứ tự hiển thị ─────────────────────
CATEGORY_ORDER_ROW1 = ["🫀 Tim mạch", "🫁 Hô hấp", "🔬 Nội tiết", "🦷 Răng Hàm Mặt"]

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
