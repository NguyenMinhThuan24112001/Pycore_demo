"""Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
"""
# n = int(input("nhập vào n : "))
# with open("file_test_mt.txt", 'w', encoding='utf-8') as f:
#     f.write("nguyen minh thuan\n")
#     f.write("nguyen thi ngoc anh\n\n")
#     f.write("contains three lines\n")
#     f.write("chung ta la 1\n")
# with open('file_test_mt.txt', 'r', encoding='utf-8') as f:
#     for i in range(n):
#         line = f.readline().rstrip("\n")
#         print(f'Dòng {i+1}: {line}')
"""Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file"""
# strs = input("nhập vào chuỗi bạn cần thêm")
# with open("file_test_mt.txt", 'r', encoding ='utf-8') as f:
#     f.write("\n" + strs + "\n")
"""Bài 03: Viết chương trình trộn 2 file thành file mới"""
# with open("file_test_mt.txt", 'r', encoding ='utf-8') as f:
#     line1 = f.read()
# with open("file_test_open.txt", 'r',encoding='utf-8') as f:
#     line2 = f.read()
# with open("file_test_ghep.txt", 'w',encoding='utf-8') as f2:
#     f2.write(line1 + line2)
"""Bài 04: Viết hàm
#         def get_file_size(file)
#     để lấy và trả về dung lượng của file"""
# import os
# def kichthuocfile(file):
#     return os.path.getsize(file)
# file1 = 'file_test_mt.txt'
# file2 = 'file_test.txt'
# print(f'kích thước của {file1} là {kichthuocfile(file1)}')
"""Viết hàm
#         def extract_characters(*files)
#     trả lại tập các ký tự trong các file"""

# square = lambda x: x * x  # Đây là hàm lambda, x là tham số, x * x là biểu thức
# print(square(5))
# a = (1,2,3,4,5)
# b = set(a)
# print(b)
# def extract_characters(*files):
#     res = set()
#     for file in files:
#         with open(file, 'r', encoding='utf-8') as fread:
#             res.update(set(fread.read()))
#     return res
#
# f1, f2, f3 = 'file_test_mt.txt', 'file_test.txt', 'file_test_open.txt'
# print(f'Các ký tự trong các file là: {extract_characters(f1, f2, f3)}')
"""# Bài 06: Viết chương trình tạo ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt"""
# import string
#
# upper_char = string.ascii_uppercase
# for c in upper_char:
#     os.mkdir(f"{c}.txt")
"""Bài 07: Đoạn chương trình sau in ra gì?"""
number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")
"""Bài 08: Đoạn chương trình sau thực viện việc gì?"""
try:
    r = 1/10
except (TypeError, ZeroDivisionError, IndentationError):
    print("Python Quiz")
"""Bài 09: Kết quả output của đoạn chương trình sau là gì?"""


def hoan_function():
    try:
        print('Monday')
    finally:
        print('Sunday')


hoan_function()
"""Bài 10: Kết quả của đoạn chương trình sau là gì?"""
try:
    print("throw")
except:
    print("except")
finally:
    print("finally")


