#Câu 6: Những giá trị nào có thể xuất hiện trong randrange(0, 100)
'''
Yêu cầu:
Những giá trị nào có thể xuất hiện khi chạy randrange(0, 100)?
4.5, 34, -1, 100, 0, 99
'''
import random
def check_randrange_values():
    possible_values = [4.5, 34, -1, 100, 0, 99]
    found_values = set()
    # Chạy randrange nhiều lần để kiểm tra các giá trị có thể xuất hiện
    for _ in range(10000):
        value = random.randrange(0, 100)
        if value in possible_values:
            found_values.add(value)
    return found_values
result = check_randrange_values()
print("Những giá trị có thể xuất hiện trong randrange(0, 100):", result)