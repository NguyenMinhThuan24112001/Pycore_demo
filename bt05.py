"bài 00 unpacking"
# a_tuple = ('nguyễn', 'thị', 'ngọc', 'ánh', 1, 2, 3 )
# a, b, c, d, e, f,g = a_tuple
# print(f"a={a}, b={b}, c={c},d={d},e={e},f={f},g={g}")
"bài btvn"
#set1 = {'python', 1,2,3,4,'hi', 6}
# set1.add(5)
# print(set1)
# set1.update([5,6,7],(8,9))
# print(set1)
# set1.clear()
# print(set1)
# set1.copy()
# print(set1)
#set2 = {'python', 1,2,3,4,7,9,'Ánh' }
# print(set1.difference(set2))
#print(set2.difference(set1))
# set2.difference_update(set1)
# print(set2)
#print(set2 - set1)
# my = [1,2,3,4,6,10,-2,5]
# set3 = {3, 4, 6, 2, 8, 9,}
# print(max(my))
# print(min(my))
# print(max(set3))
# print(min(set3))
"""bài 01 Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple"""
#a_list = [1, 2, 3, 9, 'hi', 5]
# a_tuple = (1, 2, 3, 'ha', 'hu',)
# a1_list = list(a_tuple)
# a1_tuple = tuple(a_list)
# print(a1_list)
# print(a1_tuple)
# print(a_tuple[::-1])
"""bài 03 Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple"""
# a_list = [1, 2, 3, ['Ngọc', 'Ánh'], 5, (6, 7, 4), 'hi',('ha', 'lu')]
# dem = 0
# for i in a_list:
#     if type(i) == tuple:
#         break;
#     else:
#         dem += 1
# print("dem = ", dem)
"""bài 04 Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#     Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]"""
# a = [(2, 5), (4, 1), (0, 0)]
# temp = []
# n = len(a)
# for i in range(n):
#      for j in range(i+1,n):
#          if a[i][-1] > a[j][-1]:
#              a[i], a[j] = a[j], a[i]
# print(a)
"""Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple"""

# list_demo = [(0, 1), (3, 2, 0), (0, -1), (4, 5), (9, 2), (4, 1)]
# n = len(list_demo)
# amin = list_demo[0][1]
# atuple = list_demo[0]
# for i in range(n):
#     if amin > list_demo[i][1]:
#         amin = list_demo[i][1]
#         atuple = list_demo[i]
# print("tuple thoa man {}" .format(atuple))
"""bài 7 Viết chương trình kiểm tra 2 tuple có phần tử chung hay không"""
# tuple_1 = (0, 3, 5, 7, 9, 10)
# tuple_2 = (4, 5, 9, 10, 12, -4)
# flag = False
# for i in tuple_1:
#     if i in tuple_2:
#         flag = True
# print(flag)
"""bài 8 Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không."""
# tuple_the_same = (0, 0.0, 0**1, 0*9, 0/2)
# if tuple_the_same.count(tuple_the_same[0]) == len(tuple_the_same):
#     print('giống')
# else:
#     print('không giống')
"""bài 9 Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực."""
# tuple_float = (0.1, -2.17, 200/11, 3.3, 5/6, -4/7, 11.01)
# print(sum(tuple_float))
# print(max(tuple_float))
# sum1 = 0
# max1 = tuple_float[0]
# for i in tuple_float:
#     sum1 += i
#     if max1 < i:
#         max1 = i
# print(f"tổng là {sum1}, max là {max1}")
"""# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên."""
# a_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
# b_list = []
# for i in a_list:
#     b_list.append(i.split('.')[-1])
# print(b_list)
"""# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím."""
a = input("nhập vào 1 câu : ")
b = a.strip().split(' ')
c = b[0]
for i in b:
    if len(i)>len(c):
        c = i
print(c)