1. Hướng dẫn chạy:
	Chạy cmd, vào folder chứa bài và chạy lệnh: python rundemo.py ${name}
	Với ${name} là một trong các giá trị:
		valid_insert.txt
		valid_update.txt
		valid_update_content.txt
		valid_delete.txt
		invalid_insert.txt
		invalid_update.txt
		
2. Các chức năng đã test: 5 chức năng
	Thêm một môn học
	Thay đổi thông tin môn học
	Thay đổi nội dung môn học
	Xoá môn học
	Xoá nội dung môn học
	
3. Số lượng các test đã viết: 18

4. Số lượng pass, số lượng fail: 17 pass, 1 fail

5. Các lỗi phát hiện được:
	(*) Lỗi thấy nhưng không test được
	Thêm một môn học:
		* Số tiết trên tuần không nhận được, mặc định trả về 0
		Thêm môn học có số tiết >10 cần hiện thông báo nhưng không hiện gì
	Xoá một môn học:
		Thông báo "Gặp sự cố khi gửi dữ liệu tới máy chủ" nhưng vẫn thực hiện được
		
6. Khó khăn khi thực hiện:
	Textbox giáo viên kiểu auto complete không xử lý được
	Sau khi xoá môn học, CSDL không khôi phục lại id cũ được -> Việc test tự động gặp khó khăn