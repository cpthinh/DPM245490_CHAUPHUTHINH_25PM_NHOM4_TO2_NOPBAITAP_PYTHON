#Câu 18: Vẽ các hình dưới đây
'''
Yêu cầu:
Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây:
Hình 1:             
* * * *
*     *
*     *
* * * *
Hình 2:
      *
    * *
  * * *
* * * *
Hình 3:
*
* *
*   *
* * * * * * *
        *   *
          * *
            *
'''
n = int(input("Nhập chiều cao của hình: "))
#Hình 1
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()  # Dòng trống giữa các hình
#Hình 2
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
print()  # Dòng trống giữa các hình
# Hình 3: tam giác trái (hollow) có đáy đầy, sau đó tam giác ngược dịch sang bên phải
width = 2 * n - 1
# Phần trên (từ hàng 0 tới hàng n-1)
for i in range(n):
    for col in range(width):
        if i == n - 1:
            # hàng đáy: in đầy đủ sao
            print("*", end=" ")
        else:
            # cạnh trái luôn tại col 0; cạnh phải của hàng i tại col = 2*i
            if col == 0 or col == 2 * i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

# Phần dưới: tam giác ngược, dịch dần sang phải
for b in range(n - 1):
    left = 2 * (b + 1)
    right = width - 1
    for col in range(width):
        if col == left or col == right:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()