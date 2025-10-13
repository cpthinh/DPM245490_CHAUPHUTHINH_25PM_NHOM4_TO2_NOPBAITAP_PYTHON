#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
operator = input("Nhập phép toán (+, -, *, /): ")
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        result = "Lỗi: Không thể chia cho 0"
else:
    result = "Phép toán không hợp lệ"
print(f"Kết quả: {result}")