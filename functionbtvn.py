"""Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào"""
# import  math
# def max_min(*numbers):
#     maxx = -math.inf
#     minn = math.inf
#     for n in numbers:
#         if n > maxx:
#             maxx = n
#         if n < minn:
#             minn = n
#     return maxx,minn
# a = max_min(5,6,4,3,7,8,9,10,12,11)
# print(f'max,min = {a}' )
"""Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str"""
# def reversestring(str):
#     print(str[len(str)::-1])
# reversestring('nguyen minh thuan')
# def reversestring2(str):
#     return str[::-1]
# print(f'KQ: {reversestring2("nguyen minh thuan")}')
"""Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không."""
# def perfect_number(n):
#     summ = 0
#     for i in range(1,n):
#         if n % i == 0:
#             summ += i
#     if summ == n :
#         return True
#     else:
#         return False
# n = int(input("nhập n : "))
# print(f'KQ: {perfect_number(n)}')
"""Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False"""
# def prime_number(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return False
#     return True
# n = int(input("nhập vào n: "))
# print(f'KQ:{prime_number(n)}')
"""Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str"""
# def stringing(strs):
#     dem1 = 0
#     dem2 = 0
#     for i in strs:
#         if 'a' <= i <= 'z':
#             dem1 += 1
#         if 'A' <= i <= 'Z':
#             dem2 += 1
#     print(f'số kí tự thường là {dem1},số kí tự hoa là {dem2}')
# strs = input("nhập vào chuỗi")
# stringing(strs)
"""Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần"""
# def pangram(strs,pan):
#     for i in pan:
#         if i not in strs:
#             return False
#     return True
# strs = input("nhập vào chuỗi str : ")
# pan = input("nhập vào chuỗi pan : ")
# print(f'KQ: {pangram(strs,pan)}')
# def is_pangram(str, alphabet):
#     for c in alphabet:
#         if c not in str:
#             return False
#     return True
#
#
# str = '3010120130121'
# alphabet = '0123'
# print(f'{str} là Pangram? {is_pangram(str, alphabet)}')
"""Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j"""
# import random
# def randoma(n,m):
#     return [[random.randrange(10) for j in range(m)] for i in range(n)]
# n, m = 5, 4
# res = randoma(n, m)
# print(f'Matrix {n}x{m}:')
# for i in range(n):
#     print(res[i])
"""Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
"""
# def BMI(cc,cn):
#     return cn/(cc ** 2)
# def chisoBMI(cc,cn):
#     bmi = BMI(cc,cn)
#     print(f'Your BMI:{BMI(cc,cn)}')
#     if bmi < 15:
#         print('=>> Very severely underweight')
#     elif 15 <= bmi < 16:
#         print('=>> Severely underweight')
#     elif 16 <= bmi < 18.5:
#         print('=>> Underweight')
#     elif 18.5 <= bmi < 25:
#         print('=>> Normal (healthy weight)')
#     elif 25 <= bmi < 30:
#         print('=>> Overweight')
#     elif 30 <= bmi < 35:
#         print('=>> Obese Class I (Moderately obese)')
#     elif 35 <= bmi < 40:
#         print('=>> Obese Class II (Severely obese)')
#     else:
#         print('=>> Obese Class III (Very severely obese)')
#
# cc = float(input("nhập vào chiều cao của bạn : "))
# cn = float(input("nhập vào cân nặng của bạn : "))
# chisoBMI(cc,cn)
"""Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str"""
# def chuyenkitu(strs):
#     res = []
#     for i in strs:
#         if 'a' <= i <='z':
#             res.append(chr(ord(i)-32))
#         elif 'A' <= i <= 'Z':
#             res.append(chr(ord(i)+32))
#         else:
#             res.append(i)
#     return ''.join(res)
# strs = input("chuỗi cần nhập : ")
# print(f'Chuỗi mới {chuyenkitu(strs)}')
"""Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)"""
# def demle(n):
#     if n < 10:
#         return n % 10
#     else:
#         return (n % 10) % 2 + demle(n // 10)
# print(demle(1992456))
"""Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy"""


# def de_quy_tribo(n):
#     if n < 2:
#         return 1
#     elif n == 3:
#         return 2
#     else:
#         return de_quy_tribo(n-1) + de_quy_tribo(n-2) + de_quy_tribo(n-3)
# n = int(input("nhập vào số n "))
# print(f'số tribo thứ n là : {de_quy_tribo(n)}')
def tribo(n):
    f1,f2,f3 = 1,1,2
    f = 0
    if n < 2:
        f = f2
    elif n == 3:
        f = f3
    else:
        for i in range(4,n+1):
            f = f1 + f2 + f3
            f1 = f2
            f2 = f3
            f3 = f
    return f
n = int(input("nhập vào số n : "))
print(f'số tribo thứ n là : {tribo(n)}')
"""Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1"""
# def vitri(a_list, x):
#     ok = False
#     res = []
#     for i in range(len(a_list)):
#         if a_list[i] == x:
#             res.append(i)
#             ok = True
#     if ok == True:
#         return res
#     else:
#         return -1
# a_list = [1, 2, 3, -4, 5, 6, 8, 9, 0, 3, 2, 1, 4, 5]
# x = 7
# print(vitri(a_list,x))
