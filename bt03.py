"""bài 1"""
# s1 = input("nhập vào một chuỗi :")
# if len(s1) > 0:
#     print(s1.replace(s1[0],'$'))

"""bài 2"""
# s_02 = input("Nhập vào một chuỗi: ")
# if s_02:
#     m = int(input("Vị trí muốn xóa: "))
#     if 0 <= m < len(s_02):
#         s_new = s_02[:m] + s_02[m+1:]
#         print("Chuỗi mới: " + s_new)
#     else:
#         print('Không thể tìm được vị trí cần xóa!')
# print('Bài 02 - DONE!')
"""bài 3"""
# s3 = input("nhập vào một chuỗi :")
# s_moi = s3[::2]
# print("chuỗi mới : " + s_moi)
"""bài 4"""
# ("chuỗi mới" + " s4 = input("nhập vào chuỗi : ")
# if len(s4) >= 2:
#     s = s4[:2:1] + s4[len(s4)-2: len(s4):1]
#     print(" chuỗi mới: " + s)
# else:
#     print")
s_04 = input("Nhập vào một chuỗi: ")
s_new = ""
if len(s_04) >= 2:
    s_new = s_04[0:2] + s_04[-2:]
print("Chuỗi mới: " + s_new)