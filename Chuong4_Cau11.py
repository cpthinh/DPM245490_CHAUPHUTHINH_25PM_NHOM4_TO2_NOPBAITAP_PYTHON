#Câu 11: Kiểm tra kết quả thực hiện
'''
Yêu cầu:
Cho 3 hàm dưới đây:
def sum1(n):
 s = 0
 while n > 0:
 s += 1
 n -= 1
 return s
def sum2():
 global val
 s = 0
 while val > 0:
 s += 1
 val -= 1
 return s
def sum3():
 s = 0
 for i in range(val, 0, -1):
 s += 1
 return s
Hãy cho biết kết quả sau khi gọi các lệnh dưới đây:
Trường hợp 1:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum2())
 print(sum3())
main()
Trường hợp 2:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum3())
 print(sum2())
main()
Trường hợp 3:
def main():
 global val
 val = 5
 print(sum2())
 print(sum1(5))
 print(sum3())
main()
'''
def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
# Trường hợp 1
def main1():
    global val
    val = 5
    print(sum1(5))  # Kết quả: 5
    print(sum2())   # Kết quả: 5
    print(sum3())   # Kết quả: 0
main1()
print("-----")
# Trường hợp 2
def main2():
    global val
    val = 5
    print(sum1(5))  # Kết quả: 5
    print(sum3())   # Kết quả: 5
    print(sum2())   # Kết quả: 0
main2()
print("-----")
# Trường hợp 3
def main3():
    global val
    val = 5
    print(sum2())   # Kết quả: 5
    print(sum1(5))  # Kết quả: 5
    print(sum3())   # Kết quả: 0
main3()