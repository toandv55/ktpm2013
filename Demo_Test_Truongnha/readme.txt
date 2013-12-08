>Hướng dẫn cài đặt robotframework-selenium:
1. Cài Python 2.7.6
2. Tải file này về : https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
3. Thêm vào PATH đường dẫn tới python, Gõ lệnh : python ez_setup.py (file tải ở trên)
4. Thêm vào PATH C:/Python27/Scripts
easy_install robotframework
easy_install selenium
easy_install robotframework-seleniumlibrary
easy_install robotframework-selenium2library

**********************************************
>Chạy các ví dụ demo

**Demo Login**
1. Vào thư mục Test_Login
2. Gõ python rundemo.py valid_login.txt
3. Thay file valid_login.txt bằng các file khác trừ file resource.txt

**Demo Giáo viên : thêm, xoá , sửa**
1. vào thư mục Test_Teacher
2. Gõ python rundemo.py valid_insert.txt
3. Thay file valid_insert.txt bằng các file khác trừ file resource.txt

**Demo Class và Demo môn học làm tương tự**