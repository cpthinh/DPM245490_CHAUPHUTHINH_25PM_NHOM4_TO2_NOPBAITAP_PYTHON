#Câu 19: Tính giá trị biểu thức S
'''
Yêu cầu:
Nhập x, n. TínhS(x, n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
'''
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
for i in range(n + 1):
    numerator = x ** (2 * i + 1)  # Tử số: x^(2i+1)
    denominator = 1               # Mẫu số: (2i+1)!
    for j in range(1, 2 * i + 2):
        denominator *= j
    S += numerator / denominator
print("Giá trị của S(x, n) là:", S)
