class SinhVien:
    def __init__(self, ma_sv, ten_sv, diem_toan, diem_van, diem_hoa):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_hoa = diem_hoa

    def diem_trung_binh(self):
        return (self.diem_toan + self.diem_van + self.diem_hoa) / 3

# danh sách sinh viên
danh_sach_sv = [
    SinhVien("SV1", "Nguyễn Văn A", 7.5, 8.0, 6.5),
    SinhVien("SV2", "Trần Thị B", 6.0, 7.0, 8.0),
    SinhVien("SV3", "Phạm Văn C", 4.5, 5.0, 6.0),
    SinhVien("SV4", "Lê Thị D", 8.0, 7.5, 9.0),
    SinhVien("SV5", "Hoàng Văn E", 5.5, 6.0, 4.0)
]

# các sinh viên có điểm trung bình lớn hơn 5
print("Sinh viên có điểm trung bình lớn hơn 5:")
for sv in danh_sach_sv:
    if sv.diem_trung_binh() > 5:
        print(f"Mã SV: {sv.ma_sv}, Tên SV: {sv.ten_sv}, Điểm trung bình: {sv.diem_trung_binh()}")

# các sinh viên có điểm hóa dưới 5
print("\nSinh viên có điểm hóa dưới 5:")
for sv in danh_sach_sv:
    if sv.diem_hoa < 5:
        print(f"Mã SV: {sv.ma_sv}, Tên SV: {sv.ten_sv}, Điểm hóa: {sv.diem_hoa}")
