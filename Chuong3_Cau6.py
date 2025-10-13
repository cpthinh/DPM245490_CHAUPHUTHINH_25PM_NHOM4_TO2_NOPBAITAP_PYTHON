#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ. (vd: n=35 => Ba mươi lăm, n=5 => năm).
n = int(input("Nhập một số có tối đa 2 chữ số: "))
if n < 0 or n > 99:
    print("Số không hợp lệ. Vui lòng nhập số từ 0 đến 99.")
else:
    so_hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    so_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 10:
        print(so_don_vi[n])
    elif n < 20:
        if n == 10:
            print("mười")
        elif n == 15:
            print("mười lăm")
        else:
            print("mười " + so_don_vi[n % 10])
    else:
        hang_chuc = n // 10
        don_vi = n % 10
        if don_vi == 0:
            print(so_hang_chuc[hang_chuc])
        elif don_vi == 5:
            print(so_hang_chuc[hang_chuc] + " lăm")
        else:
            print(so_hang_chuc[hang_chuc] + " " + so_don_vi[don_vi])