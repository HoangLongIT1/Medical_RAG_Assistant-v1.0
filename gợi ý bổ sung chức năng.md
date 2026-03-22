Dự án hiện tại đã có nền tảng rất vững về RAG (Tìm kiếm tri thức) và xử lý lâm sàng. Để dự án trở nên chuyên nghiệp và thực tế hơn, bạn có thể cân nhắc phát triển thêm theo 3 hướng chính sau:

*   **Hệ thống chat có nhớ ngữ cảnh (Chat History):** Hiện tại Tab 2 đã có lịch sử chat, nhưng Tab 1 (Chẩn đoán) đang chạy theo từng ca đơn lẻ. Bạn có thể thêm khả năng hỏi đáp tiếp nối về kết quả chẩn đoán đó (ví dụ: "Tại sao bạn lại loại trừ khả năng suy tim ở ca này?").

*   **Xử lý hình ảnh y tế (Multimodal):** Tận dụng khả năng Vision của Gemini để bác sĩ có thể chụp ảnh kết quả xét nghiệm máu (phiếu in giấy), ảnh chụp X-quang hoặc điện tâm đồ (ECG) rồi gửi lên cùng với mô tả ca bệnh. 

*   **Tính toán thang điểm lâm sàng:** Tích hợp các công cụ tính điểm tự động như thang điểm SOFA (nhiễm trùng huyết), CHA2DS2-VASc (nguy cơ đột quỵ), hoặc GOLD (COPD) ngay trong luồng hội thoại.

*   **Gợi ý mã ICD-10:** Sau khi đưa ra chẩn đoán, AI có thể tự động gợi ý mã ICD-10 tương ứng để bác sĩ điền vào hồ sơ bệnh án nhanh hơn.



Viết docs các tính năng hiện có của project này -> đưa cho AI gene ra các test case để test các tính năng này -> nếu có lỗi thì sửa lại code để pass các test case

