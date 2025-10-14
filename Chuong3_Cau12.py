#Câu 12: Xuất bảng cửu chương
'''
Yêu cầu:
Xuất bảng cửu chương 2→9 theo bảng sau:
2 x 1 = 2   3 x 1 = 3   ... 9 x 1 = 9
2 x 2 = 4   3 x 2 = 6   ... 9 x 2 = 18
...         ...         ...
2 x 10 = 20 3 x 10 = 30 ... 9 x 10 = 90
'''
def print_multiplication_table():
    for i in range(1, 11):  # Vòng lặp cho các số từ 1 đến 10
        for j in range(2, 10):  # Vòng lặp cho các bảng cửu chương từ 2 đến 9
            print(f"{j} x {i} = {j * i}", end="\t")  # In kết quả với tab làm khoảng cách
        print()  # Xuống dòng sau mỗi hàng
print_multiplication_table()
