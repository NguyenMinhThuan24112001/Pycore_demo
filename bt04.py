"""bài 1 Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc."""
# import random
# s1 = [3, 5, 'thuan', 8, 'anh', 4, 10, 6 ,9]
# random.shuffle(s1)
# s2 = s1[:5]
# print("list mới = ", s2)
# import random
#
# list_goc = [0, 1, 2, 'boy', 1-2j, 5, 8, 9, 4, 'a']
# random.shuffle(list_goc)  # Sẽ trộn ngẫu nhiên các phần tử trong list_goc => tạo ra đc thứ tự ngẫu nhiên
# list_moi = list_goc[:5]  # Lấy ra 5 phần tử đầu => đc list chứa 5 phần tử ngẫu nhiên
# print(list_moi)
"""Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list."""
# s = [4,2,1,6,7,5,8,9]
# tong = 0
# tich = 1
# for i in s:
#     tong = tong + i
#     tich *= i
# print(f"tổng của list là {tong}, tich của list là {tich}")
"""Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list."""
# import math
# s = [3, 4, 5, 2, 1, 6, 8, 9, 11]
# maxn = s[0]
# minn = s[0]
# for i in s:
#     if i > maxn:
#         maxn = i
#     if i < minn:
#         minn = i
# print(f"max của list là {maxn}, min của list là {minn}")
"""Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ."""
# s = ["Tôi rất yêu ", "cùng nhau nhé ", "cố gắng vì "]
# s1 = input("nhập vào chuỗi s1 = ")
# s3 = []
# for i in s:
#     s3.append(i + s1)
# print("list mới là", s3)
"""cách 2 bài 3"""
# s = ["Tôi rất yêu ", "cùng nhau nhé ", "cố gắng vì "]
# s1 = input("nhập vào chuỗi s1 = ")
# s3 = [i + s1 for i in s]
# print(s3)
"""# Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím."""
# s = [0,2,3,4,5,6,1,9,8]
# s1 = int(input("nhập vào độ dài phần đầu "))
# t = s[:s1]
# t1 = s[s1:]
#print(f"phần đầu{t}, phần sau{t1}")
"""Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
#         Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng."""
# list_05 = [0, 2, 3, 4, 5, 8, 9, 6, 7, 4, 3, 1, 3, 4, 2, 8, 0, 1, 5, 6]
# most_item = 0
# most_count = 0
# for item in list_05:
#     count_item = list_05.count(item)
#     if most_count < count_item:
#         most_count = count_item
#         most_item = item
# print(f"Giá trị: {most_item} xuất hiện {most_count}")
"""# Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau"""
# s = ['most', 'anh', 'Viet', 'hoanh', 'b', 'ba', 'a', 'bcd', 'effe', 'nan', 'two', 'xxx', 'xyx']
# dem = 0
# for i in s:
#     if len(i) >= 2 and (i[0] == i[-1]):
#         dem += 1
#
# print(f"có {dem} chuỗi thỏa mãn")
"""# Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không."""
# s1 = ['b', 'ba', 'a', 'bcd', 'effe', 0, 3.0, 6, 1.7, 8, 4.13]
# s2 = ['xb', 2, 3.3, 'b5a', 4.13, 'a9', 'bd', 'effect', 1.7, 8]
# chung = False
# for x in s1:
#     if x in s2:
#         chung = True
#         break;
# print(chung)
"""Bài 08: Cho list các số nguyên dương A.
#         Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j."""
a = [1, 3, 6, 8, 4, 9, 0, 4, 5, 6, 2, 4, 7, 9, 4, 2]
n = len(a)
dem = 0
for i in range(n-1):
    for j in range(i+1,n,1):
        if a[i]>a[j]:
            dem += 1
print(dem)