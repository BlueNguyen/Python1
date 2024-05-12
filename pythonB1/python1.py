class SinhVien:
    def __init__(self, ma_sv, ten_sv, diem_toan, diem_van, diem_hoa):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_hoa = diem_hoa

    def diem_trung_binh(self):
        diem_tb = (self.diem_toan + self.diem_van + self.diem_hoa) / 3
        return round(diem_tb, 2)

# Tạo danh sách sinh viên
danh_sach_sv = [
    SinhVien("SV001", "Nguyen Van A", 7, 8, 0),
    SinhVien("SV002", "Tran Thi B", 5, 6, 4),
    SinhVien("SV003", "Le Van C", 6, 7, 8),
    SinhVien("SV004", "Pham Thi D", 4, 5, 6),
    SinhVien("SV005", "Hoang Van E", 8, 9, 0)
]

# In thông tin các sinh viên có điểm trung bình lớn hơn 5
print("Các sinh viên có điểm trung bình lớn hơn 5:")
for sv in danh_sach_sv:
    if sv.diem_trung_binh() > 5:
        print(f"Mã SV: {sv.ma_sv}, Tên SV: {sv.ten_sv}, Điểm TB: {sv.diem_trung_binh()}")

# In ra các sinh viên có điểm hoá dưới 5
print("\nCác sinh viên có điểm hóa dưới 5:")
for sv in danh_sach_sv:
    if sv.diem_hoa < 5:
        print(f"Mã SV: {sv.ma_sv}, Tên SV: {sv.ten_sv}, Điểm Hóa: {sv.diem_hoa}")
