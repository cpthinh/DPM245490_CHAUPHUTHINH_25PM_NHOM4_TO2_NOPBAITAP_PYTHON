#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau
'''
Yêu cầu:
Nhập n. Tính S(n) = sprt(2 + sqrt(2 + sqrt(2 + ... (n lần)))), có n dấu căn lồng nhau
'''
import math
#Nhập n
n = int(input("Nhập n (số nguyên dương): "))
#Khởi tạo giá trị ban đầu của S
S = 0
#Tính S(n) bằng cách lặp n lần
for _ in range(n):
    S = math.sqrt(2 + S)
#Xuất kết quả
print(f"S({n}) =", S)
