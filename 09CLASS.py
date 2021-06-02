# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"


""" class, object là gì?
    - Python là ngôn ngữ lập trình hướng đối tượng. Không giống như ngôn ngữ lập trình hướng thủ tục, trọng tâm là hàm,
    lập trình hướng đối tượng nhận mạnh vào đối tượng - object
    - object đơn giản chỉ là tập các dữ liệu (biến) và các phương thức hoạt động trên dữ liệu đó. class là bản thết kế cho object
    - Ví dụ, class như bản phác thảo (nguyên mẫu) cho một ngồi nhà, trong đó mô tả về sàn, tường, cửa sổ, ...
    Dựa vào đó, để đi xây dựng ngôi nhà - đây chính là object
    Nhiều ngôi nhà có thể được tạo ra từ một bản thiết kế => tạo ra nhiều object từ một class
    Mỗi object được gọi là instance (thể hiện) cho class, việc tạo ra object này còn được gọi là instantiation - khởi tạo
"""

""" Định nghĩa class:
    - Bắt đầu bằng từ khóa class, sau đó là tên của nó
    - Đoạn string đầu tiên được gọi là docstring - mô tả về class. Dù nó là ko bắt buộc, nhưng nên viết nó
    => như Ví dụ 1
    - Một class sẽ tạo ra một không gian cục bộ mới, nơi mà thuộc tính - attribute của nó được định nghĩa.
    Thuộc tính có thể là data hay function
    - Ngoài ra, còn có các thuộc tính đặc biệt được định nghĩa bắt đầu bằng 2 gạch dưới __, ví dụ: __doc__ trả lại docstring của class đó
    - Ngay khi định nghĩa class, thì một class object mới được tạo ra với cùng tên.
    Cái này giúp cho phép truy cập các thuộc tính và khởi tạo đối tượng mới cho class đó => Xem ví dụ 2
"""
# Ví dụ 1:
class MyClass:
    """ This is a docstring. I have created a new class """
    pass


# Ví dụ 2:
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


""" Tạo object
    - Mỗi class object dùng để truy cập vào thuộc tính khác nhau
    - Nó cũng có thể dùng để tạo ra các object mới (thể hiện của class). Cách dùng như một lời gọi hàm => Ví dụ 3: Tạo ra
    một object có tên là obj. Có thể truy cập đến các thuộc tính của object bằng cách dùng tên của object đó.
    - Thuộc tính có thể là data hoặc method. Method của một object là các hàm tương ứng của class. Bất kì function object
    nào là thuộc tính của class đều được xác định là một method cho object của class đó.
    Điều này có nghĩa là MyClass.func là một function object (attribute của class), obj.func là method object
"""
# Ví dụ 3:
obj = MyClass()

# Ví dụ 4:
class MyClass:
    """ Đây là docstring của MyClass """
    attr = 0

    def func(self):
        print('Hallo!')


obj = MyClass()
print(MyClass.func)  # Truy cập vào hàm của class => chính là function object
print(obj.func)  # Truy cập và hàm của class => chính là method object
obj.func()  # Gọi hàm func()  # Yêu cầu object thực thi method của nó


# Để ý, trong class, có tham số self trong định nghĩa function, nhưng khi gọi obj.func() lại ko cần tham số => nó vẫn chạy
# Điều này là do, bất cứ khi nào một đối tượng gọi method của nó, chính là sẽ được truyền làm tham số đầu tiên
# Vì vậy, obj.func() được dịch thành MyClass.func(obj)
# => Túm lại thì, việc gọi phương thức với 1 list n tham số là việc gọi hàm tương ứng với list tham số được tạo ra bằng cách
# thêm object trước tham số đầu tiên. Vì vậy, đối số đầu tiên của hàm trong class phải là chính đối tượng đó,
# điều này được gọi là self, có thể dùng từ khác nhưng khuyên chân thành là nên tuân theo quy ước dùng self.
# Giờ thì đã biết đến: class object, instance object, function object, method object (và sự khác nhau giữa chúng)


""" Constructor - Hàm Khởi tạo
    - Các hàm trong class mà được bắt đầu bằng __ được gọi là các hàm đặc biệt và chúng mang nghĩa đặc biệt
    - Một trong số chúng cần quan tâm đặc biệt là __init__(). Nó sẽ được gọi khi một đối tượng mới được tạo ra
    => Hàm kiểu này, trong OOP được gọi là Constructor
    - Thương dùng để khởi tạo sẵn cho các thuộc tính
"""

class Fraction:
    def __init__(self, tu=0, mau=1):
        self.tu_so = tu
        self.mau_so = mau

#    def show(self):
#print(f'Phân số: {self.tu_so}/{self.mau_so}')


#ps1 = Fraction(1, 3)
#ps1.show()

#ps2 = Fraction(3, 5)
#ps2.attr = 7
#print(ps2.tu_so, ps2.mau_so, ps2.attr)

#print(ps1.attr)  # AttributeError: 'Fraction' object has no attribute 'attr'

# Trong đoạn code trên, định nghĩa một class mới Fraction biểu diễn cho phân số, có hai hàm
# __init__() để khởi tạo các biến tử số và mẫu số, mặc định là 0 và 1
# và show() để hiển thị phân số đúng cách
# Một thứ rất thú vị, thuộc tính của một đối tượng có thể được tạo ra khi đang chạy chương trình.
# Thấy thuộc tính attr của ps2 được tạo ra và được đọc bình thường, còn ps1 thì ko có, cố tính truy cập sẽ báo lỗi


""" Xóa bỏ thuộc tính và đối tượng
    - Bất kì thuộc tính nào của đối tượng cũng có thể bị xóa bỏ đi bất cứ lúc nào bằng cách dùng câu lệnh del => Ví dụ 5"""

# Ví dụ 5:
ps3 = Fraction(2, 5)
del ps3.mau_so
#ps3.show()  # AttributeError: 'Fraction' object has no attribute 'mau_so'

del Fraction.show
ps3.show()  # AttributeError: 'Fraction' object has no attribute 'show'

ps4 = Fraction(5, 9)
del ps4
ps4  # NameError: name 'ps4' is not defined

# Giải thích: xóa bỏ đối tượng, trong thực tế cũng khá phức tạp
# Khi tạo ra ps4 = Fraction(5, 9) một đối tượng của Fraction được tạo ra trong memory và ps4 được gắn với nó
# Trong lệnh, del ps4 cái liên kết gắn đó bị xóa và tên ps4 được xóa bỏ khỏi không gian các tên biến.
# Và đối tượng thì vẫn tồn tại trong memory, khi ko còn tên nào được gắn với nó thì nó sẽ bị hủy tự động
# Việc hủy tự động các đối tượng không có tham chiếu này trong Python được gọi là bộ sưu tập rác - garbage collection
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
# Ví dụ về kế thừa

class DaGiac:
    """ class mô tả về đa giác là hình kín, có từ 3 cạnh trở lên,
        thuộc tính n - lưu số cạnh,
        thuộc tính sides - lưu độ dài các cạnh
        phương thức input_sides - yêu cầu người dùng nhập độ dài các cạnh
        phương thức display - hiển thị độ dài các cạnh
        phương thức perimeter - tính và hiển thị chu vi
    """
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(no_sides)]

    def input_sides(self):
        self.sides = [float(input('Nhập cạnh ' + str(i+1) + ': ')) for i in range(self.n)]

    def display(self):
        for i in range(self.n):
            print(f'Side {str(i+1)} is {self.sides[i]}')

    def perimeter(self):
        print(f'Chu vi là {sum(self.sides)}')


import math


class TamGiac(DaGiac):
    """ class mô tả về tam giác, kế thừa từ đa giác
        có thêm phương thức area để tính diện tích của nó
    """

    def __init__(self):
        DaGiac.__init__(self, 3)

    def area(self):
        a, b, c = self.sides
        p = (a + b + c)/2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Diện tích của Tam giác là: %0.5f' % area)


tamgiac = TamGiac()
tamgiac.input_sides()
tamgiac.display()
tamgiac.perimeter()
tamgiac.area()

# Không định nghĩa phương thức input_sides(), display(), perimeter() cho class TamGiac nhưng vẫn có thể dùng bình thường
# Khi 1 thuộc tính không có trong class, sẽ tìm kiếm lên class cơ sở, và cứ thế tiếp tục nếu như class cơ sở là dẫn xuất của class khác


""" Method Overriding - Ghi đè phương thức
    - Trong chương trình trên thấy, __init__() được định nghĩa trong cả 2 class.
    - Điều gì xảy ra, khi method trong class dẫn xuất ghi đề lên class cơ sở
    => __init__() trong lớp dẫn xuất được ưu tiên hơn trong class cơ sở
    - Khi ghi đè, thường chúng ta mong muốn mở rộng nó chứ không đơn thuần là thay thế nó.
    Điều tương tự cũng được thực hiện khi gọi phương thức class cơ sở từ trong class dẫn xuất DaGiac.__init__(self, 3) từ __init__() của TamGiac
    Một cách tốt hơn làm việc này là dùng super()
            DaGiac.__init__(self, 3)  <=>  super().__init__(3)
"""
""" Python cung cấp isinstance() và issubclass() để kiểm tra tính kế thừa
    isinstance() - trả lại True nếu object là thể hiện của class hoặc của class dẫn xuất từ nó.
                   Tất cả các class trong Python đều được kế thừa từ class có tên là object
    issubclass() - kiểm tra kế thừa của 2 class
"""

print(isinstance(tamgiac, TamGiac))
print(isinstance(tamgiac, DaGiac))
print(isinstance(tamgiac, int))
print(isinstance(tamgiac, object))

print(issubclass(TamGiac, DaGiac))
print(issubclass(DaGiac, TamGiac))
print(issubclass(bool, int))


""" Đa kế thừa - Multiple Inheritance
    - Giống như một số ngôn ngữ lập trình khác (như C++, ...), Python cung cấp đa kế thừa
    - Một class có thể được kế thừa từ nhiều class cơ sở
    - Tất cả các thứ của các lớp cơ sở đều kế thừa lại cho class dẫn xuất
    - Cú pháp:
        class Base1:
            thân_của_Base1
        class Base2:
            thân_của_Base2
        class MultiDerived(Base1, Base2):
            thân_của_MultiDerived
"""

""" Kế thừa đa cấp - Multilevel Inheritance
    - Có thể dùng kế thừa từ một lớp dẫn xuất => kế thừa đa cấp. Trong Python, độ sâu bao nhiêu cũng được
    - Trong kế thừa đa cấp, toàn bộ trong class cơ sở và class dẫn xuất được kế thừa lại cho class dẫn xuất mới
    - Cú pháp:
        class Base:
            thân_của_Base
        class Derived1(Base):
            thân_của_Derived1
        class Derived2(Derived1):
            thân_của_Derived2
"""

""" Thứ tự các Resolution
    - Mọi class trong Python đều kế thừa từ class object - đây là class cơ sở nhất
    - Về mặt kỹ thuật, tất cả các class (kể cả dựng sẵn hay do người dùng định nghĩa) đều là class dẫn xuất của class object,
    và tất cả các đối tượng đều là thể hiện của class object => Ví dụ dưới
    - Trong kích bản đa kế thừa, bất kì thuộc tính nào đầu tiên cũng được tìm kiếm tại class hiện tại, nếu không thấy,
    sẽ tìm kiếm lên các lớp cha theo độ ưu tiên: chiều sâu - trước rồi từ trái qua phải, đảm bảo ko tìm kiếm cùng 1 class 2 lần
    Ví dụ: MultiDerived được tìm kiếm theo thứ tự [Base1, Base2, object] - tuyến tính hóa của class MultiDerived,
    quy tắc ngày được gọi là Method Resolution Order (MRO) - Thứ tự phân giải phương thức
    - MRO đảm bảo 1 class luôn xuất hiện trước cha của nó. Được hiển thị bằng thuộc tính __mro__ hoặc phương thức mro() => Ví dụ dưới
"""

print(issubclass(list, object))
print(isinstance(1992, object))
print(isinstance("Python", object))


class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


print(MultiDerived.__mro__)
print(MultiDerived.mro())

""" Một ví dụ phức tạp hơn 1 chút cho MRO - hình diễn giải: mro.jpg """

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
""" OOPs trong Python
    - Python là một trong những ngôn ngữ lập trình đa mô hình => Python sẽ hỗ trợ nhiều phương pháp lập trình khác nhau
    - Một trong những phương pháp tiếp cận phổ biến hiện nay là Hướng đối tượng - Object-Oriented Programming (OOP)
    - Một đối tượng có hai đặc trưng:
        - Thuộc tính (attributes)
        - Hành vi (behavior)
    - Xét ví dụ sau:
        Cat là một đối tượng có:
        - tên, tuổi, màu lông => Thuộc tính
        - kêu, chạy, nhảy, ăn, uống => Hành vi
    - Khái niệm OOP trong Python còn tập trung vào việc viết code có thể tái sử dụng, được biết đến như là DRY - Dont Repeat Yourself
    - Trong Python, OOP theo một số nguyên tắc cơ bản như sau:
        - Inheritance - Kế thừa: Sử dụng các chi tiết từ một class mới mà ko làm thay đổi gì class đã có
        - Encapsulation - Đóng gói: Ẩn các chi tiết riêng tư của một class đối với các object khác
        - Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào khác nhau
"""

""" Class - Là bản thiết kế cho object
    - Có thể hình dùng class như một bản phác thảo của một cat với các nhãn. Nó chứa tất cả chi tiết về name, age, ...
    - Dựa trên các mô tả đó, chúng ta sẽ đi tìm hiểu về cat, ở đây, cat là một object
"""
class Cat:
    pass
# Sử dụng keyword class để định nghĩa một class Cat - rỗng. Từ class, chúng ta sẽ khởi tạo được instance.
# Một instance là một đối tượng riêng biệt từ lớp cụ thể


""" Object
    - Một object (instance) là một khởi tạo của một lớp
    - Khi class được định nghĩa, thì chỉ có các mô tả của object được xác định
    => không có bộ nhớ hoặc lưu trữ nào được phân bổ
"""
obj_cat = Cat()
# Ở đây, obj_cat là object của class Cat

# Chúng ta đã nói chi tiết về Mèo - Cat rồi, giờ sẽ cũng nhau đi xây dựng chi tiết về class và về object của Cat như sau:
class Cat:
    # class attribute - thuộc tính của class
    loai = 'Thú họ Mèo'

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


# instance of Cat class - Khai báo 2 đối tượng của class Cat
muop = Cat('Mướp', 2, 'Vàng')
mun = Cat('Mun', 1, 'Đen')

# Truy cập class attribute
print(f'Mướp là', muop.__class__.loai)
print(f'Mun cũng là', mun.__class__.loai)

# Truy cập instance attribute
print(f'{muop.name} đã {muop.age} tuổi và lông màu {muop.color}')
print(f'{mun.name} đã {mun.age} tuổi và lông màu {mun.color}')

# Trong đoạn chương trình trên, đã tạo ra một class Cat với các attribute và các attribute là những đặc trưng của từng object
# Sau đó, tạo 2 object của Cat là muop và mun
# Truy cập đến thuộc tính class (class attribute) bằng __class__.loai. Các class attribute sẽ là như nhau với mọi object của Cat
# Truy cập đến instance attribute bằng muop.name, muop.age, ... Các instance attribute của các object sẽ là khác nhau


""" Method - Là các định nghĩa hàm bên trong thân class, dùng để định nghĩa hành vi của object """

# Ví dụ: Tạo method trong Python
class Cat:
    # class attribute - thuộc tính của class
    loai = 'Thú họ Mèo'

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # instance method
    def run(self):
        return f'{self.name} đang chạy'

    def eat(self, f):
        return f'{self.name} thích ăn {f}'


cam = Cat('Cam', 2, 'Vàng, Trắng')

# call instance methods
print(cam.run())
print(cam.eat('pate gan'))

# Ở trên chúng ta định nghĩa 2 method: run() và eat(), đây được gọi là instance method vì chúng chỉ được gọi qua một instance object


""" Inheritance - Kế thừa
    - Là cách tạo ra class mới có sử dụng chi tiết từ class đã có mà ko thay đổi nó
    - Lớp mới được gọi là lớp dẫn xuất (hoặc lớp con), lớp đã có là lớp cơ sở (hoặc lớp cha)
"""
# Ví dụ:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Tạo Person!')

    def who_am_i(self):
        print('Person')

    def speak(self, lang='Tiếng Việt'):
        print(f'{self.name} nói {lang}')


class StudentIT(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        print('Tạo StudentIT!')

    def who_am_i(self):
        print('StudentIT')

    def code(self, lang):
        print(f'{self.name} lập trình {lang}')


svbk = StudentIT('CườngĐM', 30, 'HUST')
svbk.who_am_i()
svbk.speak()
svbk.code('Python')

# Trong đoạn chương trình trên, chúng ta tạo ra 2 class: Person (cha) và StudentIT (con).
# Class con kế thừa toàn bộ các hàm của class cha, có thể nhìn thấy method speak()
# Tiếp đến, class con đã thay đổi hành vi của class cha với method who_am_i()
# Hơn nữa, class con mở rộng class cha với method code()
# Thêm đó, sử dụng super().__init__() vì muốn kéo toàn bộ __init__() của class cha vào class con


""" Encapsulation - Đóng gói
    - Trong Python, có thể hạn chế quyền truy cập vào các phương thức và biến => ngăn dữ liệu ko bị sửa đổi trực tiếp
    => được gọi là Đóng gói - Encapsulation
    - Dùng ký hiệu cho thuộc tính private là 2 gạch dưới __
"""
# Ví dụ
class Laptop:

    def __init__(self):
        self.__price = 500

    def sell(self):
        print(f'Giá bán là {self.__price}')

    def set_price(self, price):
        self.__price = price


lap = Laptop()
lap.sell()

# thay đổi giá trị price, cố tình truy cập vào thuộc tính
lap.__price = 1000
lap.sell()

# thay đổi qua hàm setter
lap.set_price(1000)
lap.sell()

# Trong chương trình trên, khai báo một class Laptop, trong method __init__() lưu giá của laptop đó.
# Cố gắng thay đổi giá, tuy nhiên, ko thể, vì python coi __price là thuộc tính private
# Để thay đổi giá thì ta dùng qua setter: set_price() với tham số là giá mới
# Cách để lấy giá của các thuộc tính ra thì dùng hàm getter, ở đây chính là sell()


""" Polymorphism - Đa hình
    - Là khả năng (trong OOP) cho phép dùng chung interface cho nhiều hình thái (kiểu dữ liệu)
    - Ví dụ cho dễ hiểu: Cần tô màu cho một hình, có nhiều hình: vuông, tròn, chữ nhật, ...; nhưng có thể dùng cùng một
    phương thức để tô màu cho hình => Đây chính là đa hình
"""
# Ví dụ:
class PC:
    def wifi(self):
        print('Không kết nối được!')


class Laptop:
    def wifi(self):
        print('Kết nối được rồi!')


def connect_wifi(computer):
    computer.wifi()


lap = Laptop()
pc = PC()

connect_wifi(lap)
connect_wifi(pc)

# Trong đoạn chương trình trên, tạo 2 class PC và Laptop, mỗi cái đều có method wifi(); tuy nhiên, chúng khác nhau
# Để kiểm tra về đa hình, tạo ra hàm connect_wifi() nhận bất kì object.
# Truyền vào hàm đó đối tượng lap và pc và chạy nó xem kết quả.

""" Lưu ý:
    - Lập trình trở lên dễ dàng và hiệu quả
    - Class có thể chia sẻ, nên code có thể sử dụng lại
    - Năng suất của chương trình tăng
    - Dữ liệu được an toàn và bảo mật với sự trừu tượng hóa dữ liệu
"""