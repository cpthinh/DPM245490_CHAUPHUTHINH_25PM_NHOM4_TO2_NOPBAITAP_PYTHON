#Câu 10: Tính dãy số
'''
Yêu cầu:
Cho biểu thức toán học sau:
 Tính S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!
 Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức.
'''
x = float(input("Nhập x: "))
n = int(input("Nhập n (số nguyên dương): "))
if n <= 0:
    print("n phải là số nguyên dương.")
else:
    S = 0
    factorial = 1  # Biến lưu giai thừa
    for i in range(1, n + 1):
        factorial *= i  # Tính giai thừa i
        S += (x ** i) / factorial  # Cộng liên tục vào S
    print(f"Kết quả S({x}, {n}) = {S}")
