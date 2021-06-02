# sum = 0
# while True:
#     n = float(input("nhap n = "))
#     if(n<1000):
#         while n > 0:
#                 m = n%10
#                 n = n // 10
#                 sum += m
#         break;
#     else:
#         print("Bạn đã nhập sai")
# print("Tổng các chữ số của n = ", sum)
# while True:
#     n = int(input("Nhập giá trị n dương (< 1000): "))
#     if 0 < n < 1000:
#         break
#     print("Nhập chưa đúng, hãy nhập lại!")
#
# tong = 0
# m = n
# while n > 0:
#     tong += n % 10
#     n //= 10
# print(f"Tổng các chữ số của {m} là {tong}")
a = float(input("nhap a = "))
b = float(input("nhap b = "))
c = float(input("nhap c = "))
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("là độ dài của 3 cạnh tam giác")
        if (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
            print("đây la tam giác vuông")
        else:
            print("đây không là tam giác vuông")
    else:
        print("đây không phải tam giác")
else:
    print("đây không phải tam giác")
