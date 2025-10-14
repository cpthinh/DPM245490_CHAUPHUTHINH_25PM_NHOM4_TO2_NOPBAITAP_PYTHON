#Câu 15: Giải thích cách chạy các dòng lệnh range
'''
Yêu cầu:
(a) range(5)
(b) range(5, 10)
(c) range(5, 20, 3)
(d) range(20, 5, -1)
(e) range(20, 5, -3)
(f) range(10, 5)
(g) range(0)
(h) range(10, 101, 10)
(i) range(10, -1, -1)
(j) range(-3, 4)
(k) range(0, 10, 1)
'''
print("range(5):", list(range(5)))  # Tạo danh sách từ 0 đến 4
print("range(5, 10):", list(range(5, 10)))  # Tạo danh sách từ 5 đến 9
print("range(5, 20, 3):", list(range(5, 20, 3)))  # Tạo danh sách từ 5 đến 19 với bước nhảy là 3
print("range(20, 5, -1):", list(range(20, 5, -1)))  # Tạo danh sách từ 20 đến 6 với bước nhảy là -1
print("range(20, 5, -3):", list(range(20, 5, -3)))  # Tạo danh sách từ 20 đến 6 với bước nhảy là -3
print("range(10, 5):", list(range(10, 5)))  # Tạo danh sách rỗng vì không thể đi từ 10 đến 5 với bước nhảy mặc định là 1
print("range(0):", list(range(0)))  # Tạo danh sách rỗng
print("range(10, 101, 10):", list(range(10, 101, 10)))  # Tạo danh sách từ 10 đến 100 với bước nhảy là 10
print("range(10, -1, -1):", list(range(10, -1, -1)))  # Tạo danh sách từ 10 đến 0 với bước nhảy là -1
print("range(-3, 4):", list(range(-3, 4)))  # Tạo danh sách từ -3 đến 3
print("range(0, 10, 1):", list(range(0, 10, 1)))  # Tạo danh sách từ 0 đến 9 với bước nhảy là 1
print()