import math
# n = int(input("nhap n = "))
# x = int(input("nhap x = "))
# s1 = 0
# s2 = 0
# s = 0
# for i in range(n+1):
#     s += x ** i
# print("tong s = ", s)
# for i in range(n+1):
#     if i%2 == 0:
#         s1 += x ** i
#     else:
#         s2 -= x ** i
# print(f"tổng của s = ", s1+s2)
# for i in range(n+1):
#     s += (x ** i) / math.factorial(i)
# print(f"tong s = ", s)
x = float(input("Nhập x: "))
n = int(input("Nhập n:"))
S3 = 0
for i in range(n+1):
    S3 += x ** i / math.factorial(i)
print(f"Giá trị S3 = {S3}")
