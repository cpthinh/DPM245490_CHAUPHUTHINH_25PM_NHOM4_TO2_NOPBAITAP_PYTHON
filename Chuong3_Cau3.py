#Câu 3: Phương trình bậc 2
'''
Yêu cầu: Viết chương trình giải phương trình bậc 2: ax^2+bx+c=0
'''
import math
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c/b
        print("Phương trình có một nghiệm x =", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)