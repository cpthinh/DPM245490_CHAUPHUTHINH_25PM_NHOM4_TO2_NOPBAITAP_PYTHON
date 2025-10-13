#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Ngày tháng không hợp lệ.")
else:
    if month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = 31

    if day > max_day:
        print("Ngày không hợp lệ cho tháng đã cho.")
    else:
        # Tính ngày kế tiếp
        if day < max_day:
            day += 1
        else:
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

        print(f"Ngày kế tiếp là: {day}/{month}/{year}")