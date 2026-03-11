Một số chức năng cần điều chỉnh sau khi deploy lên Streamlit Cloud và test:

1. Mục Chọn nhanh các ca bệnh mẫu(Dành cho Demo): Nên chỉnh sửa lại các câu hỏi trong các test cases đó. Đề xuất thay đổi: Nên tạo thành các ô chứa các testcase mỗi khoa và hỗn hợp (tim mạch, hô hấp, nội tiết, tim +hô hấp, tim + nội tiết, nội tiết + hô hấp, tim + hô hấp + nội tiết) -> mỗi khi user nhấn vào ô bất kì, nó sẽ load ra câu hỏi tương ứng mỗi chuyên khoa(và hỗn hợp) vào trong ô đặt câu hỏi -> điểm khác là mỗi khi user nhấn lại nó sẽ load ra câu hỏi khác nhau (ví dụ ấn 2 lần vào khoa tim mạch thì load 2 bệnh sử và triệu chứng khác nhau - các bệnh sử và triệu chứng phải được reset ngẫu nhiên và đủ độ dài, độ chi tiết) -> tăng độ ngẫu nhiên cũng như thách thức khả năng của AI hơn.

2. Phần UX/UI: Nên sửa lại cách load thông tin và load câu trả lời --> nên thống nhất thành 1 thể cho gọn và đỡ rối.

3. Tab 2 - phân tích phác đồ(file tải lên): Sửa lại để có chức năng tải lên nhiều file cùng lúc (giới hạn nên được tăng: tối đa 10-20 file, tối đa mỗi file 100mb, tối đa tổng file < 2GB)

4. Bổ sung thêm chức năng xuất câu trả lời ra file DOCX (đã có xuất ra markdown và PDF) và khi xuất thì câu trả lời trên web vẫn giữ nguyên để user còn đọc(hiện tại khi xuất thì câu trả lời được hiển thị sẽ lập tức mất đi).
