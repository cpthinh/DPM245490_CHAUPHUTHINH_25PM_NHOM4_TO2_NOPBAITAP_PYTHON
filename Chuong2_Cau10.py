#Câu 10: Hãy viết ngắn gọn lại các lệnh dưới đây
'''
Yêu cầu:
Cho các lệnh ban đầu:
(a) x = x + 1
(b) x = x / 2
(c) x = x - 1
(d) x = x + y
(e) x = x - (y + 7)
Trang 21/84
(f) x = 2*x
(g) number_of_closed_cases = number_of_closed_cases + 2*ncc
Hãy viết ngắn gọn lại lệnh.
'''
#Giải:
#Gán cho các biến x, y, ncc một giá trị ban đầu để chạy chương trình
x = 1
y = 2
ncc = 3
print("a)", x := x + 1)#a) x = x + 1 => x += 1
print("b)", x := x / 2)#b) x = x / 2
print("c)", x := x - 1)#c) x = x - 1 => x -= 1
print("d)", x := x + y)#d) x = x + y => x += y
print("e)", x := x - (y + 7))#e) x = x - (y + 7) => x -= (y + 7)
print("f)", x := 2*x)#f) x = 2*x => x *= 2
print("g)", ncc := ncc + 2*ncc)#g) number_of_closed_cases = number_of_closed_cases + 2*ncc => number_of_closed_cases += 2*ncc