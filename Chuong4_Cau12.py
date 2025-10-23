#Câu 12: Hàm oscillate
'''
Yêu cầu:
Cho mã lệnh:
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
Hãy viết hàm oscillate để khi chạy phần mềm, nó sẽ ra kết quả:
    -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
'''
def oscillate(start, end):
    result = []
    for i in range(abs(start), abs(end) + 1):
        if i != 0:
            result.append(-i)
        result.append(i)
    return result
for n in oscillate(-3, 5):
    print(n, end=' ')
print()