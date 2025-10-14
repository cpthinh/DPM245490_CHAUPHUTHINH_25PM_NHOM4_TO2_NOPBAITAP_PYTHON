#Câu 11: Kiểm tra số nguyên tố
'''
Yêu cầu:
Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    while True:
        try:
            num = int(input("Nhập vào một số nguyên: "))
            if is_prime(num):
                print(f"{num} là số nguyên tố.")
            else:
                print(f"{num} không phải là số nguyên tố.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
        
        cont = input("Bạn có muốn tiếp tục không? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thoát chương trình.")
            break
if __name__ == "__main__":
    main()