#Câu 13: Cho biết bao nhiêu dấu * được in ra trên màn hình
'''
Yêu cầu:
Nhập vào a và cho biết bao nhiêu dấu * được in ra trên màn hình:
a = 0
while a < 100:
    print("*", end='')
print()
'''
a = int(input("Nhập vào a: "))
count = 0
while a < 100:
    print("*", end='')
    count += 1
    a += 1
print()
print(f"Có {count} dấu * được in ra trên màn hình")


