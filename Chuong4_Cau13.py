#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
'''
Yêu cầu:
Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không?
(Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number)hay
không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn
nó.
'''
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
def is_perfect_number(n):
    return sum_of_divisors(n) == n
def is_abundant_number(n):
    return sum_of_divisors(n) > n

def main():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương!")
        return
    if is_perfect_number(n):
        print(f"{n} là số hoàn thiện.")
    else:
        print(f"{n} không phải là số hoàn thiện.")
    if is_abundant_number(n):
        print(f"{n} là số thịnh vượng.")
    else:
        print(f"{n} không phải là số thịnh vượng.")

if __name__ == "__main__":
    main()