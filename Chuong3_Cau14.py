#Câu 14: Cho biết bao nhiêu dấu * được in ra trên màn hình
'''
Yêu cầu:
Nhập vào a và b. Cho biết bao nhiêu dấu * được in ra trên màn hình:
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print("*", end='')
        b += 1
    print()
    a += 1
'''
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
count = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print("*", end='')
            count += 1
        b += 1
    print()
    a += 1
print(f"Có {count} dấu * được in ra màn hình")
print()
