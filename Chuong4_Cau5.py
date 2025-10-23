#Câu 5: Viết hàm đệ qui Fibonacci
'''
Yêu cầu:
Dãy Số Fibonacci là dãy số có dạng:
1→1→2→3→5→8→13→21→34→55→89…
Được định nghĩa theo công thức đệ qui như dưới đây:
Nếu N=1,N=2➔FN=1
N>2 FN=FN-1+FN-2
Hãy viết 2 hàm:
- Hàm trả về số Fib tại vị trí thứ N bất kỳ
- Hàm trả về danh sách dãy số Fib từ 1 tới N
'''
def fibonacci(n):
    if n <= 0:
        return "Vị trí phải là số nguyên dương."
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_list(n):
    if n <= 0:
        return "N phải là số nguyên dương."
    fib_list = []
    for i in range(1, n + 1):
        fib_list.append(fibonacci(i))
    return fib_list
# Nhập dữ liệu từ người dùng
n = int(input("Nhập vào vị trí N để tìm số Fibonacci: "))
fib_number = fibonacci(n)
print(f"Số Fibonacci tại vị trí {n} là: {fib_number}")
fib_list = fibonacci_list(n)
print(f"Dãy số Fibonacci từ 1 tới {n} là: {fib_list}")