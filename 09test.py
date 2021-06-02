class MyClass:
    """ Đây là docstring của MyClass """
    attr = 0

    def func(self):
        print('Hallo!')


obj = MyClass()
print(MyClass.func)  # Truy cập vào hàm của class => chính là function object
print(obj.func)  # Truy cập vào hàm của class => chính là method object
obj.func()  # Gọi hàm func()  # Yêu cầu object thực thi method của nó
class MyClass:
    """ Đây là docstring của MyClass """
    attr = 0

    def func(self):
        print('Hallo!')


print(MyClass.__doc__)
print(MyClass.attr)
print(MyClass.func)
ok = MyClass()
ok.func()

class funtion:
    def __init__(self, tu=0,mau=1):
        self.tu_so = tu
        self.mau_so = mau
    def show(self):
        print(f"phân số có dạng:{self.tu_so}/{self.mau_so}")
phanso = funtion(1,3)
phanso.show()
phanso1 = funtion(3,5)
phanso1.attr = 7
print(phanso1.tu_so,phanso1.mau_so,phanso1.attr)
# ps3 = funtion(2, 5)
# del ps3.mau_so
# ps3.show()  # AttributeError: 'Fraction' object has no attribute 'mau_so'
#
# del funtion.show
# ps3.show()  # AttributeError: 'Fraction' object has no attribute 'show'
#
# ps4 = funtion(5, 9)
# del ps4
# ps4  # NameError: name 'ps4' is not defined
a = [0 for i in range(10)]
print(a)
""" Inheritance - Kế thừa là gì?
    - Kế thừa là một tính năng rất mạnh mẽ trong lập trình hướng đối tượng OOP
    - Đề cập đến việc tạo ra một class mới bằng việc ít hoặc không sửa đổi một class đã có.
    class mới được gọi là class dẫn xuất (con), class mà nó kế thừa được gọi là class cơ sở (cha)
    - Cú pháp:
        class BaseClass:   #class cơ sở
            thân_của_BaseClass
        class DerivedClass(BaseClass):   #class dẫn xuất
            thân_của_DerivedClass
    - class dẫn xuất thừa hưởng toàn bộ từ class cơ sở (=> Khả năng tái sử dụng code), và có thể được thêm các tính năng mới
"""
class Dagiac:
    def __init__(self,no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(self.n)]
    def input_sides(self):
        self.sides = [float(input("nhập cạnh " + str(i+1)+ ": ")) for i in range(self.n)]
    def output_sides(self):
        for i in range(self.n):
            print(f'cạnh {str(i+1)} là {self.sides[i]}')
    def chuvi(self):
         return (f'chu vi là {sum(self.sides)}')
a = Dagiac(6)
a.input_sides()
a.output_sides()
# a.chuvi()Bayes Classifier
#a = Dagiac(6)
print(a.chuvi())
import math
class Tamgiac(Dagiac):
    def __init__(self):
        #Dagiac.__init__(self,3)
        super(Tamgiac,self).__init__(3)
    def area(self):
        a,b,c = self.sides
        p = (a + b + c) / 2
        areaa = math.sqrt(p * (p-a) * (p-b) *(p-c))
        print(f'diện tích tam giác {areaa}')
b =Tamgiac()
b.input_sides()
b.output_sides()
b.chuvi()
b.area()
