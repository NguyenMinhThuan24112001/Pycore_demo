import math
# r = float(input("nhập vào bán kính hình tròn :"))
# b = math.pi
# s = b * r * r
# print("dien tích của hình tròn đó {}" .format(round(s,3)))
"""Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>"""
# import math
# a = float(input("nhập vào số a : "))
# b = float(input("nhập vào số b : "))
# c = float(input("nhập vào số c : "))
# f = (a+b+c) / (a ** 2 + b ** 2 + 1) - abs(a-c * math.cos(b))
# print(f)
"""Lập chương trình thực hiện các công việc sau:
    Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    Tính tổng các chữ số của số đó.
    Hiển thị kết qủa ra màn hình
"""
# while True:
#      n = int(input("nhập vào số nguyên dương n = "))
#      if 0 < n < 1000:
#          break
#      print("nhập chưa đúng hãy nhập lại")
# tong = 0
# while n > 0:
#      tong += n % 10
#      n //= 10
# print(tong)
# while True:
#     n = int(input("Nhập giá trị n dương (< 1000): "))
#     if 0 < n < 1000:
#         break
#     print("Nhập chưa đúng, hãy nhập lại!")
#
# tong = 0
# while n > 0:
#     tong += n % 10
#     n //= 10
# print(f"Tổng các chữ số của {n} là {tong}")
"""Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $."""
#s = input("nhập vào chuỗi : ")
# if len(s) > 0:
#     b = s.replace(s[0],'$')
#     print(b)
"""Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím"""
# if s:
#     m = int(input("nhập từ bàn phím :"))
#     if 0 < m < len(s):
#         print(s[:m]+s[m+1:])
#     else:
#         print("không có phần tử để xóa")
"""Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi."""
"""Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
# nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng"""
# s1 = " "
# if len(s) > 2:
#     s1 = s[:2] + s[-2:]
#     print(s1)
# else:
#     print(s1)
"""Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím."""
# c1 = s[0]
# c2 = s[0]
# for i in s:
#     if c1 > i:
#         c1 = i
#     elif c2 < i:
#         c2 = i
# print(c1, c2)
# s_05 = input("Nhập vào một chuỗi: ")
# if s_05:
#     c_max, c_min = s_05[0], s_05[0]
#     for c in s_05:
#         if c > c_max:
#             c_max = c
#         elif c < c_min:
#             c_min = c
#     print(f"Ký tự lớn nhất {c_max} và nhỏ nhất {c_min}")
"""Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi."""
"""Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc"""
# import random
# a_list = ['hi', 'ha',1, 2, 3, 4, 5, 'haha']
# random.shuffle(a_list)
# print("5 phân tử của list gốc là ", a_list[:5])
"""Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list."""
#alist = [-4, 9, 3, 4, 5, -8, 2, 1, -6, 3]
# tong = 0
# tich = 1
# for i in alist:
#     tong  += i
#     tich *= i
# print(f"tổng của list là {tong}, tích của list là {tich}")
#print(f"số lớn nhất trong list là {max(alist)}, số nhỏ nhất là {min(alist)}")
"""Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ"""
# the_list = ['girl', 'mot', 'hai', 'Hai', 'Huy', 'Cuong', 'PythonCore']
# s = input("Nhập chuỗi s: ")
# list_moi = []
# for i in the_list:
#     list_moi.append((s + i))
# print(list_moi)
# A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
# b = set(A)
# print(b)
# """Tìm phần tử có số lần xuất hiện nhiều nhất"""
# the_list = ['girl', 'mot', 'hai', 'Hai', 'Huy', 'Cuong', 'PythonCore']
# s = input("nhập vào chuỗi s : ")
# b = []
# for i in the_list:
#     b.append(i + s)
# print(b)
# list_05 = [0, 2, 3, 4, 5, 8, 9, 6, 7, 4, 3, 1, 3, 4, 2, 8, 0, 1]
# b = 0
# c = 0
# for i in list_05:
#     a = list_05.count(i)
#     if c < list_05.count(i):
#         c = list_05.count(i)
#         b = i
# print(b)
"""Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau"""
# list_06 = ['most', 'anh', 'Viet', 'hoanh', 'b', 'ba', 'a', 'bcd', 'effe', 'nan', 'two', 'xxx', 'xyx']
# dem = 0
# for i in list_06:
#     if len(i) >= 2 and (i[0] == i[-1]):
#         dem += 1
#
# print(dem)
# list_071 = ['b', 'ba', 'a', 'bcd', 'effe', 0, 3.0, 6, 1.7, 8, 4.13]
# list_072 = ['xb', 2, 3.3, 'b5a', 4.13, 'a9', 'bd', 'effect', 1.7, 8]
# a = False
# for i in list_071:
#     if i in list_072:
#         a = True
#         break
# print(a)
"""Bài 08: Cho list các số nguyên dương A.
#         Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j."""
# A = [1, 3, 6, 8, 4, 9, 0, 4, 5, 6, 2, 4, 7, 9, 4, 2]
# n = len(A)
# dem = 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if A[i] > A[j]:
#             dem += 1
# print(dem)
"""Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple"""
# list_demo = [0, 0.2, 'string', 5, [3, 2, 1], (0, ), [4, 7, 'temp']]
# dem = 0
# for i in list_demo:
#     if type(i) == tuple:
#         break
#     else:
#         dem += 1
# print(f"số lượng các phân tử thỏa mãn là {dem}")
"""Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple."""
# list_sample = [(2, 5), (4, 1), (0, 0)]
# a_list = []
# n = len(list_sample)
# for i in range(n):
#     for j in range(i+1,n):
#         if list_sample[i][-1] > list_sample[j][-1]:
#             list_sample[i],list_sample[j] = list_sample[j],list_sample[i]
# print(list_sample)
"""Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple"""
# list_demo = [(0, 1), (3, 2, 0), (0, -1), (4, 5), (9, 2), (4, 1)]
# minn = list_demo[0][1]
# item_min = list_demo[0]
# for item in list_demo:
#     if item[1] < minn:
#         minn = item[1]
#         item_min = item
# print(f'Tuple có phần tử thứ 2 là nhỏ nhất {item_min}')
"""# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không"""
# tuple_the_same = (0, 0.0, 0**1, 0*9, 0/2)
# minn = tuple_the_same[0]
# b = tuple_the_same.count(minn)
# flag = False
# if b == len(tuple_the_same):
#     flag = True
# print(flag)
"""Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên"""
# list_domain = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
# do = []
# for i in list_domain:
#     an = i.split('.')
#     do.append(an[-1])
# print(do)
"""Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím"""
str_input = input('Nhập câu văn: ')

st=str_input.strip().split(' ')
at = st[0]
maxx = len(st[0])
for i in st:
    if len(at) < len(i):
        at = i
print(at)


