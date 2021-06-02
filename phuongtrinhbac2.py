import math
a = float(input("nhập vào số a = "))
b = float(input("nhập vào số b = "))
c = float(input("nhập vào số c = "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"phương trình có nghiệm ", -c / b)
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        print(f"phuong trinh co nghiem kep ", -b / (2 * a))
    elif d > 0:
        k = math.sqrt(d)
        print(f"phương trình có nghiệm thứ nhất = ", round((-b - k) / (2 * a), 3))
        print(f"phương trình có nghiệm thứ hai = ", round((-b + k) / (2 * a), 3))
    else:
        print("Phương trình vô nghiệm")
