# import math
# x, y, z = float(input()), float(input()), float(input())
# F = (x+y+z)/(x**2+y**2+1) - math.fabs(x - z * math.cos(y))
# print("bieu thuc co gia tri la ", F)
# a = True
# b = False
# print(a + 9)
# print(b + 9)
# print("not a is", not a)
# print("not b is", not b)
# print("a or b is", a or b)
# print("a and b is", a and b)
"""phép so sánh"""
# a = 2000
# b = 3000
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
"""câu lệnh rẽ nhánh"""
""" câu lệnh if, cú pháp câu lệnh
if bieu_thuc_dieu_kien
    cac cau lenh can thuc thi neu bieu_thuc_dieu_kien la True

"""
# n = float(input("nhap vao so nguyen N la:"))
# if n>0:
#     print("N la so nguyen duong")
# else:
#     print("N khong la so nguyen duong")
# n = float(input("nhap vao so nguyen N la:"))
# if n>0:
#     print("N la so nguyen duong")
#
# print("đay la câu lệnh ngoài If")
# n = int(input("nhap vao so n ="))
# if n<0:
#     n = -n
# print("Trị tuyệt đối của n la", n)
""" câu lệnh if-elif-else"""
""" Cú pháp của if-elif-else
    if biểu_thức_điều_kiện_01:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_01 là Đúng (True)
    elif biểu_thức_điều_kiện_02:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_02 là Đúng (True)
    else:
        các câu lệnh cần chạy nếu các biểu_thức_điều_kiện ở trên đềy là Sai (False)
"""
# n = float(input("nhap vao so nguyen n = "))
# if n == 0:
#     print("n la so không")
# elif n>0:
#     print("n la so duong")
# else:
#     print("n la so am")
""" Chương trình: Nhập vào 2 số nguyên, in ra màn hình:
    + Tổng của 2 số đó, nếu cả 2 số đều dương
    + Tích của 2 số đó nếu cả 2 số đều âm
    + Nếu không in ra màn hình số nhỏ hơn trong 2 số đó
"""
# a = float(input("nhap vao so a = "))
# b = float(input("nhap vao so b = "))
# if a > 0 and b > 0:
#     print("tong cua hai so la {}" .format(a+b))
# elif a < 0 and b < 0:
#     print("tich cua hai so la {}" .format(a*b))
# else:
#     print("so nho hon la", min(a, b))
"""Vòng lặp for"""
# Ví dụ: In ra cá giá trị nguyên từ 0 đến 9
# for i in range(10):
#     print(i)

""" Hàm range(start=0, stop, step_size=1): Generate a sequence of numbers
    + start: giá trị bắt đầu sinh, mặc định = 0
    + stop: giá trị kết thúc sinh, có nghĩa là sinh đến giá trị bé hơn stop. Không có mặc định
    + step_size: bước nhảy để sinh các giá trị tiếp theo từ start (nhận cả giá trị âm và dương), mặc định = 1
"""

# for i in range(2,14,2):
#     print(i, end=" ")
# a = int(input())
# b = int(input())
# for i in range(a + 1, b, 1):
#     print(i, end=" ")
# n = int(input("nhap vao so nguyen n = "))
# s = 1
# for i in range(1, n+1, 1):
#     s *= i
# print("giai thua cua n la", s)
""" Cú pháp cho vòng while
    while biểu_thức_điều_kiện:
        các câu lệnh sẽ chạy của mỗi vòng while, một vòng while được chạy khi biểu_thức_điều_kiện là Đúng (True)
"""

# Nhập vào một số tự nhiên n rồi tính tổng các số tự nhiên đến n
# n = float(input("nhap vao so n = "))
# i = 0
# s = 0
# while i <= n:
#     s = s + i
#     i +=1
# print("tong = ", s)
while True:
    n = int(input("nhap vao so nguyen n:"))
    if n > 0:
        print("bạn đã nhập số dương, chương trình dừng lại")
        break
    print("bạn đã nhập sai, chương trình tiếp tục")
