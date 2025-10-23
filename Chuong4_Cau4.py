#Câu 4: Viết Hàm tính ROI
'''
Yêu cầu:
ROI (Return On Investment), một thuật ngữ quan trọng trong marketing, mà đặc
biệt là SEO, tạm dịch là tỷ lệ lợi nhuận thu được so với chi phí bạn đầu tư. Có thể
hiểu ROI một cách đơn giản chính là chỉ số đo lường tỷ lệ những gì bạn thu về so
với những gì bạn phải bỏ ra.
Hiểu đúng bản chất của ROI, bạn sẽ đo lường được hiệu quả đồng vốn đầu tư của
mình cho các chi phí như quảng cáo, chạy Adwords, hay chi phí marketing online
khác.
Vì ROI dựa vào các chỉ số cụ thể, nên nó cũng là một thước đo rất cụ thể:
ROI = (Doanh thu – Chi phí)/Chi phí
Viết chương trình cho phép người dùng nhập vào Doanh thu và Chi phí và xuất ra
tỉ lệ ROI cho người dùng, đồng thời hãy cho biết nên hay không nên đầu tư dự án
khi biết ROI (giả sử mức tổi thiểu ROI =0.75 thì mới đầu tư).
'''
def tinh_ROI(doanh_thu, chi_phi):
    if chi_phi == 0:
        return None  # Tránh chia cho 0
    roi = (doanh_thu - chi_phi) / chi_phi
    return roi
def danh_gia_dau_tu(roi, muc_toi_thieu=0.75):
    if roi is None:
        return "Chi phí không thể là 0."
    elif roi >= muc_toi_thieu:
        return "Nên đầu tư dự án."
    else:
        return "Không nên đầu tư dự án."
# Nhập dữ liệu từ người dùng
doanh_thu = float(input("Nhập vào Doanh thu: "))
chi_phi = float(input("Nhập vào Chi phí: "))
roi = tinh_ROI(doanh_thu, chi_phi)
print(f"Tỷ lệ ROI: {roi:.2f}" if roi is not None else "Tỷ lệ ROI không xác định.")
ket_qua = danh_gia_dau_tu(roi)
print(ket_qua)