# f1 = open('file_test_open.txt')
# f2 = open('file_test_open.txt', mode = 'r',encoding='utf-8')
# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

""" File, Directory
    - Open, Read, Write, Close File
    - Various methods with file object
    - Create, Rename, Listing Dir
"""
""" File:
    - Là nơi trên ổ cứng lưu trữ các thông tin liên quan nhau
    - Dùng để lưu trữ vĩnh viễn dữ liệu trong bộ nhớ dài hạn
    - RAM là bộ nhớ ngắn hạn, sẽ mất dữ liệu khi mất điện => Dùng file để lưu dữ liệu lại cho xử lý sau này
    - Để thao tác vào file cần phải mở nó ra trước, sau khi thao tác (đọc hoặc ghi) thì cần đóng nó lại
    Quy trình thao tác với file như sau:
        Bước 1. Mở file  =>  Bước 2. Đọc hoặc ghi (thực hiện thao tác)  =>  Bước 3. Đóng tệp
"""

""" Open file
    - Python cung cấp hàm open(), hàm trả lại một file object
    - Định nghĩa đầy đủ của hàm open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
"""
f1 = open('file_test_open.txt')  # Mở file ngay trong thư mục hiện tại chứa file chương trình
# f2 = open('/home/hoanpp/Desktop/ds_file')  # Mở file với đường dẫn đầy đủ của file

""" Các chế độ khi mở tệp cần được chỉ định, mục đích để đảm bảo an toàn thông tin cho file
    - r: Mở file để đọc (mặc định)
    - w: Mở file để ghi, tạo 1 file mới nếu như file không tồn tại hoặc truncate(xóa hết các dữ liệu) trước khi ghi
    - x: Mở file để thực thi. Nếu file không tồn tại thì thao tác mở sẽ fail
    - a: Mở file để nối thêm vào cuối file (ko truncate trước khi thêm). Tạo mới file nêu như nó không tồn tại
    - t: Mở ở chế độ văn bản (mặc định)
    - b: Mở ở chế độ nhị phân
    - +: Mở file để cập nhật (đọc và viết)
"""

f3 = open('file_test_open.txt')  # <=>  open('file_test_open.txt', 'r') hoặc open('file_test_open.txt', 'rt')
f4 = open('file_test_open.txt', 'w')  # Ghi với dạng text
f5 = open('file_test_open.txt', 'r+b')  # Đọc và ghi ở dạng nhị phân

""" Chú ý, không giống như nhiều ngôn ngữ khác,
    ký tự trong file ví dụ như a ko phải là 97 nếu như ko chỉ định sử dụng mã ASCII.
    Hơn nữa, mỗi hệ điều hành lại chọn 1 kiểu mã hóa khác nhau, Win dùng cp1252, Linux thì dùng utf-8.
    => Ko nên dùng mã hóa mặc định, vì trên mỗi hệ điều hành nó sẽ hoạt động khác nhau.
    => Khi làm việc với file văn bản thì chúng ta nên chỉ rõ lại mã hóa sẽ dùng
"""

f6 = open('file_test_open.txt', mode='r', encoding='utf-8')

""" Đóng file:
    - Khi hoàn thành các thao tác thì cần đóng file đúng cách
    - Đóng file để giải phóng các tài nguyên gắn với file
    - Hàm dùng close()
"""

f7 = open('file_test_open.txt', encoding='utf-8')
# Làm gì đó với file f7 ở trên
f7.close()

""" Nếu khi làm gì đó với file mà có lỗi thì sẽ ko thể đóng được file
    - Cách 1: Dùng thêm try-finally (sẽ được học sau)
    - Cách 2: Dùng với with - cách tốt nhất, không cần có close(), mặc định khi nào hết khối with thì file sẽ được đóng
"""

with open('file_test_open.txt', encoding='utf-8') as f:
    # Làm gì đó với file ở đây
    pass


""" Ghi dữ liệu vào file
    - Mở với chế độ ghi w, nối thêm a
    - Cẩn trọng với chế độ w, có thể bị ghi đè dữ liệu mới lên dữ diệu cũ, làm dữ liệu cũ bị xóa hết
    - Để ghi dữ liệu dùng hàm write(). Phương thức trả lại số lượng ký tự được ghi vào tệp
"""

with open("file_test_open.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
# Chương trình tạo ra file mới tên là file_test.txt trong thư mục hiện tại nếu như file đó chưa tồn tại,
# nếu có rồi thì ghi đè
# Ghi các dòng vào trong file, để ghi thành các dòng thì cần thêm các ký tự xuống dòng (\n) vào các chỗ cần thiết


""" Đọc file
    - Dùng chế độ đọc r
    - Phương thức hay dùng là read(size) dùng để đọc số lượng size dữ liệu
    - Nếu hàm trên mà ko chỉ định rõ size thì sẽ đọc đến cuối file
"""

f_read = open('file_test_open.txt', 'r', encoding='utf-8')
print(f_read.read(4))  # Đọc 4 ký tự đầu
print(f_read.read(4))  # Đọc 4 ký tự tiếp theo 4 ký tự đầu
print(f_read.read())  # Đọc tiếp đến khi nào hết dữ liệu
print(f_read.read())  # Đọc tiếp => hết file rồi nên trả về chuỗi rỗng

""" Nguyên tắc hoạt động của read là dịch chuyển một con trỏ ảo đi lần lượt các dữ liệu trong file,
    sau mỗi lần read xong số lượng mong muốn thì con trỏ đó vẫn duy trì và đứng sẵn tại đó chờ câu lệnh read tiếp theo - nếu có
    Để thay đổi vị trí của của con trỏ thì dùng hàm seek()
    Hàm tell() trả lại vị trí hiện tại (tính theo đơn vị byte)
"""

print(f_read.tell())  # Lấy vị trí hiện tại của con trỏ đọc file
f_read.seek(0)  # Cho con trỏ về lại đầu file
print(f_read.read())

""" Làm thế nào để đọc từng dòng trong file => dùng vòng lặp for, hoặc readline() hoặc readlines() """

for line in f_read:
    print(line, end='')
# Chú ý, mặc định mỗi dòng đều đã có xuống dòng, để đỡ bị dòng trắng thì ta dùng end='' cho câu lệnh print

print(f_read.readline())
print(f_read.readline())

print(f_read.readlines())  # Trả lại toàn bộ các dòng trong file dưới dạng list


""" Một số hàm hay dùng khác đối với file:
    - readable(): Trả lại True nếu luồng file có thể đọc
    - readline(n=-1): Đọc và trả lại một dòng từ file. Nếu n được chỉ định thì đọc tối đa n byte
    - readlines(n=-1): Đọc và trả về một danh sách các dòng từ file. Nếu n được chỉ định thì đọc tối đa n byte/ký tự
    - seek(offset, from=SEEK_SET): Thay đổi vị trí con trỏ file đến offset byte, tính từ from (Đầu, Hiện tại, Kết thúc)
    - seekable(): Trả lại True nếu luồng file có hỗ trợ truy cập ngẫu nhiên
    - truncate(size=None): Thay đổi size của luồng file thành size byte, nếu size ko được chỉ định, thì thay đến vị trí hiện tại
    - writable(): Trả lại True nếu luồng file cho phép ghi
    - writelines(lines): Ghi một list các dòng vào trong file
"""


""" Directory
    - Khi có nhiều file để xử lý trong chương trình Python, thì sắp xếp vào các thư mục để dễ quản lý
    - Một thư mục (directory/folder) là một tập hợp các file và thư mục con
    - Python cung cấp module os chứa nhiều phương thức để làm việc với directory (và cả file khá tốt)
"""

""" Cách lấy đường dẫn thư mục hiện tại, dùng getcwd() """

import os
print(os.getcwd())

""" Cách di chuyển sang thư mục khác dùng chdir() """
# os.chdir('/home/hoanpp/Desktop/')
print(os.getcwd())

""" Cách lấy danh sách thu mục con và file dùng listdir() """

os.chdir('/home/hoanpp/Desktop/')
print(os.listdir())  # Lấy từ thư mục đang làm việc
print(os.listdir('/home/hoanpp/Desktop/PyCore-Course'))  # Lấy từ thư mục chỉ định

""" Tạo ra thư mục mới bằng: mkdir() """

os.mkdir('test_dir')
print(os.listdir())

""" Đổi tên thư mục hoặc file, dùng rename() """
print(os.listdir())
os.rename('test_dir', 'new_test_dir')
print(os.listdir())

""" Xóa bỏ thư mục hoặc file, dùng rmdir() - cái này chỉ dùng xóa đi được thư mục rỗng,
    còn dùng rmtree() trong module shutil để remove toàn bộ thư mục,
    còn file thì dùng remove()
"""
print(os.listdir())
os.remove('file_test_open.txt')
print(os.listdir())
os.rmdir('new_one')
print(os.listdir())
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

""" Exception:
    - Handling
    - Except clause
    - try-finally clause
"""

""" Python errors và Built-in Exceptions
    - Syntax/Parsing errors: Lỗi do không tuân theo cú pháp của ngôn ngữ
    - Logical errors (Exceptions): Lỗi xảy ra trong thời gian chạy (sau khi qua kiểm tra cú pháp)
    Ví dụ:
        - Cố tình mở 1 file chưa có lên để đọc - FileNotFoundError
        - Cố tình chia cho 0 - ZeroDivisionError
        - Có tình import module không tồn tại - ImportError
        - Có tình ép kiểu không đúng - ValueError
"""
# Chạy thử các ví dụ sau
print(1/0)  # Chi cho 0
a = int('9.a')  # Ép kiểu với giá trị ko đúng định dạng số nguyên
open('file_not_found.txt')  # file không tồn tại

""" Danh sách các exception phổ biến mà python dựng sẵn ảnh common_built-in_exceptions.PNG """

""" Khi các exception xảy ra, nó sẽ làm cho chương trình bị dừng lại và chuyển lên nơi mà gọi nó,
nếu không handled thì sẽ bị crash. 
    Ví dụ: A gọi B và B gọi tiếp sang C; nếu trong C có exception mà không được handled thì nó sẽ đẩy lên B và tiếp tục lên A.
    Và cuối cùng ko được handled thì có một thông báo error hiện lên, chương trình sẽ dừng đột ngột.
    => Để bắt và xử lý được các exception thì chúng ta sẽ dùng các lệnh try, except và finally.
"""

""" Bắt exception, với ví dụ sau - chưa chỉ rõ exception cụ thể """
import sys

random_list = ['a', 0, 0.5]

for item in random_list:
    try:
        print("Phần tử:", item)
        r = 1 / int(item)
        print("Nghịch đảo của", item, "is", r)
    except:
        print("Oops!", sys.exc_info()[0], "Toang Rồi!.")  # import module sys to get the type of exception
        print("=> next \n")

""" Bắt exception, với ví dụ sau - chỉ rõ exception cụ thể """

try:
    # Code gì đó có thể gây exception
    pass

except ValueError:
    # Xử lý nếu như exception loại ValueError xảy ra
    pass

except (TypeError, ZeroDivisionError):
    # Xử lý nếu như gặp nhiều exceptions cùng lúc, ở đây đang xét 2 loại TypeError và ZeroDivisionError
    pass

except:
    # Xử lý tất cả các loại exceptions khác 3 loại trên
    pass

""" Raising Exceptions, xét các ví dụ sau để xem về việc raise exception """

raise KeyboardInterrupt

raise MemoryError("This is an argument")

try:
    a = int(input("Nhập một số nguyên dương: "))
    if a <= 0:
        raise ValueError("Số vừa nhập không phải số nguyên dương!")
except ValueError as ve:
    print(ve)

""" Dùng câu lệnh: try-finally
    - Câu lệnh try đi kèm với câu lệnh finally thì các câu lệnh trong khối finally sẽ luôn được thực thi dù có chuyện gì đi nữa!
    - Các câu lệnh trong finally thường dùng để giải phóng tài nguyên cho phần đang chạy
"""
# Nhớ lại về phần file đã có đoạn try-finally như sau:
try:
    f = open("test.txt", encoding='utf-8')
    # Làm gì đó với file trên nếu như mở thành công
finally:
    f.close()
# Luôn đảm bảo tệp được đóng ngay cả khi có ngoại lệ xảy ra.