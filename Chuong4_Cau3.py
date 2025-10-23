#Câu 3: Viết Hàm tính BMI
'''
Yêu cầu:
Gọi BMI là chỉ số cân đối cơ thể. Yêu cầu đầu vào nhập là chiều cao và cân nặng,
hãy cho biết người này như thế nào, biết rằng:
BMI = cân nặng (kg) / (chiều cao (m))^2
Hãy thông báo phân loại Và cảnh bảo nguy cơ cho họ theo bảng dưới đây:
    Phân loại            Chỉ số BMI         Nguy cơ
       Gầy                < 18.5             Thấp
   Bình thường          18.5 - 24.9       Trung bình
     Hơi béo            25.0 - 29.9           Cao
Béo phì cấp độ I        30.0 - 34.9         Rất cao
Béo phì cấp độ II       35.0 - 39.9        Nguy hiểm
Béo phì cấp độ III        >= 40.0       Cực kỳ nguy hiểm
'''
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao ** 2)
    if bmi < 18.5:
        phan_loai = "Gầy"
        nguy_co = "Thấp"
    elif 18.5 <= bmi < 25.0:
        phan_loai = "Bình thường"
        nguy_co = "Trung bình"
    elif 25.0 <= bmi < 30.0:
        phan_loai = "Hơi béo"
        nguy_co = "Cao"
    elif 30.0 <= bmi < 35.0:
        phan_loai = "Béo phì cấp độ I"
        nguy_co = "Rất cao"
    elif 35.0 <= bmi < 40.0:
        phan_loai = "Béo phì cấp độ II"
        nguy_co = "Nguy hiểm"
    else:
        phan_loai = "Béo phì cấp độ III"
        nguy_co = "Cực kỳ nguy hiểm"
    return bmi, phan_loai, nguy_co
def main():
    try:
        chieu_cao = float(input("Nhập chiều cao của bạn (cm): "))
        can_nang = float(input("Nhập cân nặng của bạn (kg): "))
        bmi, phan_loai, nguy_co = tinh_bmi(chieu_cao, can_nang)
        print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        print(f"Phân loại: {phan_loai}")
        print(f"Mức độ nguy cơ: {nguy_co}")
    except ValueError:
        print("Vui lòng nhập giá trị số hợp lệ cho chiều cao và cân nặng.")
if __name__ == "__main__":
    main()