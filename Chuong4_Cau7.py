#Câu 7: Tính và xuất độ dài đoạn AB
'''
Yêu cầu:
Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB.
Công thức: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2)
'''
import math
#Nhập toạ độ điểm A
xA = float(input("Nhập hoành độ điểm A (xA): "))
yA = float(input("Nhập tung độ điểm A (yA): "))
#Nhập toạ độ điểm B
xB = float(input("Nhập hoành độ điểm B (xB): "))
yB = float(input("Nhập tung độ điểm B (yB): "))
#Tính độ dài đoạn AB
do_dai_AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
#Xuất kết quả
print("Độ dài đoạn AB là:", do_dai_AB)