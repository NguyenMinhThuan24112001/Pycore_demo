# my_dict = {
#     'Thuận':'Ánh',
#     'yêu':'nhau',
#     'a':10
# }
# print(my_dict['Thuận'])
# print(my_dict['a'])
# print(my_dict.get('yêu'))
# print(my_dict.get('a'))
# your_dict = {
#     'a' : [(1,2,3), 5,7],
# 'b': (3,4,5),
# 1: 'age',
# }
# print(your_dict['a'])
# print(your_dict['b'])
# print(your_dict[1])
# print(your_dict.get('a'))
# my_dict = dict([(1,'mot'),(2,'hai'),(3,'ba')])
# print(my_dict)
# my_dict = {
#     'name':'Thuận',
#     'age':20,
#     'my love':'Ngọc Ánh'
# }
# my_dict['age'] = 25
# my_dict['time'] = 'forever'
# print(my_dict)
# my_dict.pop('age')
# print(my_dict)
# print(my_dict.popitem())
# print(my_dict.clear())
# del my_dict
""" Các phương thức của dict
    - clear(): Xóa toàn bộ phần tử, thành dict rỗng
    - copy(): Tạo bản sao cho dict
    - fromkeys(seq[, v]): Trả lại dict mới với các key từ seq và giá trị từ v, nếu không có thì mặc định = None
    - get(key[,d]): Trả lại value của key, nếu key ko tồn tại thì trả lại d, nếu ko có d thì trả lại None
    - items(): Trả lại thể hiện của dict dạng (key, value)
    - keys(): Trả lại List các key của dict
    - values(): Trả lại list các giá trị của các phần tử trong dict
    - pop(key[,d]): Xóa và trả lại value của phần tử có key, nếu không tồn tại key thì trả lại d, nếu ko có d thì báo lỗi KeyError
    - popitem(): Trả lại phần tử bất kì dạng (key, value), nếu dict rỗng thì báo lỗi KeyError
    - setdefault(key[,d]): Nếu key tồn tại, trả lại value, nếu ko thêm key với value=d và trả lại d, nếu ko có d thì là None
    - update([other]): Cập nhật dict với các cặp key-value trong other, nếu key tồn tại thì sẽ ghi đè
    - values(): Trả lại list các giá trị của các phần tử trong dict
"""
# my_dict = {
#     'name':'Thuận',
#     'age':20,
#     'my love':'Ngọc Ánh'
# }
# print(my_dict.copy())
# a = {}.fromkeys([1,2,3],'xl')
# print(my_dict.get('name'))
# print(my_dict.items())
# print(my_dict.setdefault('name'))
# my_dict.update({
#     'name':'Minh Thuận',
#     'ahih':'ahaha'
# })
# print(my_dict)
""" Dictionary Comprehension: Tạo dict một cách bao quát
    - Tạo dict mới từ việc duyệt lặp
    - Dạng lệnh: cặp key:value theo sau là for, tất cả đc đặt trong {}
    - Trong for có thể chứa nhiều for khác hoặc chứa if
"""
# ab = {}
# for i in range(10):
#     ab[i]= i ** 2
# print(ab)
# my_dict = {i : i ** 2 for i in range(10) if i % 3 ==0}
# print(my_dict)
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16
}
for i in my_dict:  # duyệt như này sẽ là duyệt key
    print(f"Key: {i}, value: {my_dict[i]}")

for i in my_dict.keys():
    print(f"Key: {i}, value: {my_dict[i]}")
print(len(my_dict))
print(sorted((my_dict)))