#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
month = int(input("Nhập tháng (1-12): "))
if month < 1 or month > 12:
    print("Tháng không hợp lệ.")
else:
    if month in [1, 2, 3]:
        quarter = 1
    elif month in [4, 5, 6]:
        quarter = 2
    elif month in [7, 8, 9]:
        quarter = 3
    else:
        quarter = 4
    print(f"Tháng {month} thuộc quý {quarter}.")