#Câu 1: Viết hàm để Tính diện tích tam giác
'''
Yêu cầu:
Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác, Sau đó tính diện tích
theo công thức Herong:
cv = a + b + c, p = cv / 2 và dt = sqrt(p * (p - a) * (p - b) * (p - c))
'''
import math
def tinh_dien_tich_tam_giac(a, b, c):
    # Kiểm tra tính hợp lệ của tam giác
    if a + b > c and a + c > b and b + c > a:
        cv = a + b + c
        p = cv / 2
        dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return dt
    else:
        return None
# Nhập vào 3 cạnh của tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
dien_tich = tinh_dien_tich_tam_giac(a, b, c)
if dien_tich is not None:
    print(f"Diện tích tam giác là: {dien_tich}")
else:
    print("Ba cạnh không hợp lệ để tạo thành tam giác.")