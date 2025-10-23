#Câu 8: Viết chương trình tính loga(x)
'''
Yêu cầu:
Viết chương trình tính log(a(x)) trong đó
với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
!= 1.( dùng log(a(x))=ln(x)/ln(a))
'''
import math
#Nhập cơ số a
a = float(input("Nhập cơ số a (a > 0 và a != 1): "))
#Nhập số x
x = float(input("Nhập số x (x > 0): "))
#Kiểm tra điều kiện a>0, a!=1 và x>0
if a <= 0 or a == 1:
    print("Cơ số a không hợp lệ. Vui lòng nhập lại a sao cho a > 0 và a != 1.")
elif x <= 0:
    print("Số x không hợp lệ. Vui lòng nhập lại x sao cho x > 0.")
else:
    #Tính loga(x) sử dụng công thức loga(x) = ln(x) / ln(a)
    loga_x = math.log(x) / math.log(a)
    #Xuất kết quả
    print(f"log{a}({x}) =", loga_x)