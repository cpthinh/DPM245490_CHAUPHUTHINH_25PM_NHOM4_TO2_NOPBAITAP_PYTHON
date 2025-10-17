#Câu 16: Cho biết bao nhiêu dấu * được in ra trên màn hình
'''
Yêu cầu:
Cho biết bao nhiêu dấu * được in ra trên màn hình:
for i in range(20, 100, 5):
    print('*', end=' ')
print()
'''
count = 0
for i in range(20, 100, 5):
    print('*', end=' ')
    count += 1
print()
print("Tổng số dấu * được in ra trên màn hình là:", count)
