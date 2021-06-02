"""Bài 00: Viết chương trình tính tích value của các phần tử trong một dict"""
# my_dict = {
#     0:1,
#     2:3,
#     3:4,
#     't':4,
#     'a':3
# }
# tich = 1
# # for i in my_dict:
# #     tich = tich * my_dict[i]
# # print(f'tich của value là:{tich}')
# for key,value in my_dict.items():
#     tich *= value
# print(f'tích của value:{tich}')
""" Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict"""
# import  math
# dict_01 = {
#     -2: 9,
#     0: 1,
#     2: 3,
#     'k': 4,
#     'x': 5,
#     -1: 2,
#     3: -3
# }
# maxx = -math.inf
# minn = math.inf
# for key,value in dict_01.items():
#     if value > maxx:
#         maxx = value
#     if value < minn:
#         minn = value
# print(f'value nhỏ nhất là {minn}, value lớn nhất là {maxx}')
"""bài 02: Viết chương trình lấy các các value không trùng lặp từ dict"""
# dict_02 = {
#     -2: 9,
#     'a': -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     'k': 4,
#     'x': 5,
#     0: 9,
#     'b': 3
# }
# my_set = set()
# for i in dict_02:
#     my_set.add(dict_02[i])
# print(my_set)
# my_set1 = set(dict_02.values())
# print(f'Value không trùng lặp {my_set1} ')
"""Bài 03: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict"""
# dict_03 = {
#     -2: 9,
#     4: -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     6: 4,
#     -9: 5,
#     0: 9,
#     -8: 3
# }
# sort = sorted(dict_03.keys(),reverse=True)
# abc = [(sort[0],dict_03[sort[0]]),(sort[1],dict_03[sort[1]]),(sort[2],dict_03[sort[2]])]
# print(f'3 phan tử có keys lớn nhất là{abc}')
"""Bài 04: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict"""
# dict_04 = {
#     'key1': [0, 2, 4, 1, 3, 5, 6],
#     'key2': [0, -2, 4, 1, -3, 5, 0],
#     'key3': [-2, 4, 1, -3, -5, 0],
#     'key4': [0, -2, -4, 1, -3, 5],
#     'key5': [0, 4.314, 1, -3, 5, 0.1],
# }
# for k,v in dict_04.items():
#     print(f'phần tử thú 5 của {k} là {v[4]}')
"""Bài 05: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict"""
# dict_051 = {
#     1: 1,
#     2: 2,
#     3: 3,
#     4: 5,
#     6: 7
# }
# dict_052 = {
#     1: -1,
#     2: -2,
#     -3: 3,
#     4: 5,
#     6: -7
# }
# a = set()
# for k,v in dict_051.items():
#     if k in dict_052 and v == dict_052[k]:
#         a.add((k,v))
# print(f'các cặp key,value xuất hiện trong cả 2 dict là:{a}')
"""Bài 06: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
     keys = ["name", "salary"]
     Output: {'name': 'Kelly', 'salary': 8000}"""
# sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
# keys = ["name", "salary"]
# a = {k:sampleDict[k] for k in keys}
# print(a)
"""Bài 07: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict"""
# dict_07 = {
#     -2: 9,
#     4: -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     6: 4,
#     -9: 5,
#     0: 9,
#     -8: 3
# }
# values_max_sorted = sorted(dict_07.values(), reverse=True)[0:3]
# result = set()
# for k, v in dict_07.items():
#     if v in values_max_sorted:
#         result.add((k, v))
# print(f'Kết quả của bài toán {result}')
# print(values_max_sorted)
"""Bài 08: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}"""
# input_str = 'Stringings'
# set_char = set(input_str)
# result = {}
# for c in set_char:
#     result[c] = input_str.count(c)
# print(f'Kết quả bài toán {result}')
# print(set_char)
"""Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản"""
# from string import punctuation
# import re
#
# input_09 = '''Mot cau van trong doan van. Day la vi du ve sinh doan van de tach tu don.'''
# r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
# set_word = r.split(input_09)
# result = {}
# for w in set_word:
#     result[w] = set_word.count(w)
# print(f'Kết quả của bài toán: {result}')
# print(r)
# print(set_word)
"""# Bài 10: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
# Bài 10: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}"""
# Input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Output = {}
# for i in Input:
#     name = i['item']
#     amout = i['amount']
#     if name in Output:
#         Output[name] += amout
#     else:
#         Output[name] = amout
# print(Output)
"""ài 00: Viết chương trình tính tích value của các phần tử trong một dict"""
# my_dict = {
#     'một':2,
#     3:4,
#     5:6,
#     9:-2
# }
# tich = 1
# for k,v in my_dict.items():
#     tich = tich * v
# print(tich)
"""# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict"""
# import math
# dict_01 = {
#     -2: 9,
#     0: 1,
#     2: 3,
#     'k': 4,
#     'x': 5,
#     -1: 2,
#     3: -3
# }
# maxx = -math.inf
# minn = math.inf
# for i in dict_01.values():
#     if i > maxx:
#         maxx = i
#     if i < minn:
#         minn = i
# print(f'value nhỏ nhất là{minn}, value lớn nhất là {maxx}')
"""Bài 02: Viết chương trình lấy các các value không trùng lặp từ dict"""
# dict_02 = {
#     -2: 9,
#     'a': -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     'k': 4,
#     'x': 5,
#     0: 9,
#     'b': 3
# }
# sett = set()
# for k,v in dict_02.items():
#     sett.add(v)
# print(sett)
# sett2 = set(dict_02.values())
# print(sett2)
"""Bài 03: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict"""
# dict_03 = {
#     -2: 9,
#     4: -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     6: 4,
#     -9: 5,
#     0: 9,
#     -8: 3
# }
# sort = sorted(dict_03.keys(),reverse=True)
# abc = [(sort[0],dict_03[sort[0]]),
#        (sort[1],dict_03[sort[1]]),
#        (sort[2],dict_03[sort[2]])]
#print(f'3 cặp key,values có key lớn nhất là {abc}')
"""Bài 04: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict"""
# dict_04 = {
#     'key1': [0, 2, 4, 1, 3, 5, 6],
#     'key2': [0, -2, 4, 1, -3, 5, 0],
#     'key3': [-2, 4, 1, -3, -5, 0],
#     'key4': [0, -2, -4, 1, -3, 5],
#     'key5': [0, 4.314, 1, -3, 5, 0.1],
# }
# for k,v in dict_04.items():
#     print(f'phần tử thứ năm của values trong {k} là {v[4]}')
"""Bài 05: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict"""
# dict_051 = {
#     1: 1,
#     2: -2,
#     3: 3,
#     4: 5,
#     6: 7
# }
# dict_052 = {
#     1: -1,
#     2: -2,
#     -3: 3,
#     4: 5,
#     6: -7
# }
# sett = set()
# for k,v in dict_051.items():
#     if k in dict_052 and v == dict_052[k]:
#         sett.add((k,v))
# print(sett)
"""Bài 06: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}"""
# sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
# key = ["name", "salary"]
# reu = {k:sampleDict[k] for k in key}
# print(reu)
"""Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict"""
# dict_07 = {
#     -2: 9,
#     4: -1,
#     2: 3,
#     -1: 2,
#     3: -3,
#     6: 4,
#     -9: 5,
#     0: 9,
#     -8: 3
# }
# sort = sorted(dict_07.values(),reverse=True)[0:3]
# sett = set()
# for k,v in dict_07.items():
#     if v in sort:
#         sett.add((k,v))
# print(sett)
"""Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}"""
stringg = 'Stringings'
a = set(stringg)
b = {}
for i in a:
        b[i] = stringg.count(i)
print(b)

