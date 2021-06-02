my_str = """Nguyễn Thị Ngọc Ánh
Xinh gái
Dễ thương
Hiền lành
Tốt tính
"""
# print(my_str)
# my_str1 = "Nguyễn Thị Ngọc Ánh"
# print(my_str1)
# print(my_str1 * 3)
# print(my_str1 + my_str)
"Tính độ dài chuỗi"
#print(len(my_str1))
""" Truy cập vào các ký tự của chuỗi
"""
# s = "Thuan Anh"
# print(s[0])
# print(s[1])
# print(s[len(s)-1])
# print(s[-1])
# print(s[-2])
# print(s[-len(s)])
"""Kỹ thuật đoạn cắt-slicing cơ bản"""
#s = "Python Core"
# print(s[2: 8]) #thon C
# print(s[0: 6]) #Python
#print(s[7: len(s)])
# print(s[-9: -1])
# print(s[5: -3])
# print(s[: 6])
# print(s[7:])
# print(s[:])ỹ thuật đoạ
"""kỹ thuật đọan cắt - slicing nâng cao với bước nhảy dương"""
# print(s[::2])
# print(s[1::2])
# print(s[2:-1:3])
"""kỹ thuạn đọan cắt - slicing nâng cao với bước nhảy âm"""
# print(s[8:2:-2])
# print(s[::-1])  # cách lấy ra chuỗi đảo của s
# print(s[-2::-3])
"""Toán tử in và not in"""
# s = 'Nguyễn Thị Ngọc Ánh'
# print("Nguyễn" in s)
# print("thi" in s)
# print("Ngọc Ánh" in s)
# print("Ánh" not in s)
# print("ánh" not in s)
"""Duyệt các kí tự trong chuỗi"""
"""dùng vòng for"""
# s = input("nhập vào chuỗi s = ")
# dem = 0
# for i in range(len(s)):
#     if '0' <= s[i] <= '9':
#         dem += 1
#print("so các ký tự số trong chuỗi s là", dem)
"""các hàm trong chuỗi"""
#s = ' nguyễn thị ngọc ÁNH '
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.count('us'))
# print(s.count(('n')))
"""tìm kiếm và thay thế"""
s = 'python is is amazing'
print(s.find('on'))
print(s.find('python'))
print(s.rfind('n'))
print(s.startswith('Py'))
print(s.endswith(('ing')))
print(s.replace('is', 'are'))
