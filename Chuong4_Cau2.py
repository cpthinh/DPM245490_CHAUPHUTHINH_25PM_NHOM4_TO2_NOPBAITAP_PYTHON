#Câu 2: Viết Hàm để chơi Game Đoán Số
'''
Yêu cầu:
Máy ra 1 số trong đoạn [1...100]
Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số
người chơi đoán nhỏ hơn hay lớn hơn số của mày và hiển thị số lần đoán
Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?
'''
import random
def doan_so():
    so_bi_mat = random.randint(1, 100)
    so_lan_doan = 0
    max_lan_doan = 7

    print("Chào mừng bạn đến với trò chơi Đoán Số!")
    print("Tôi đã chọn một số trong khoảng từ 1 đến 100.")
    print(f"Bạn có tối đa {max_lan_doan} lần đoán để tìm ra số đó.")

    while so_lan_doan < max_lan_doan:
        try:
            doan = int(input("Hãy nhập số bạn đoán: "))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
            continue

        so_lan_doan += 1

        if doan < so_bi_mat:
            print("Số bạn đoán nhỏ hơn số bí mật.")
        elif doan > so_bi_mat:
            print("Số bạn đoán lớn hơn số bí mật.")
        else:
            print(f"Chúc mừng! Bạn đã đoán đúng số {so_bi_mat} trong {so_lan_doan} lần đoán.")
            break
    else:
        print(f"Rất tiếc! Bạn đã hết lượt đoán. Số bí mật là {so_bi_mat}.")
    tiep_tuc = input("Bạn có muốn chơi lại không? (c/k): ").lower()
    if tiep_tuc == 'c':
        doan_so()
doan_so()
