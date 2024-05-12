class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        if self.khoaHoc:
            print(f"Danh sách khóa học của học viên {self.tenHV}:")
            for khoaHoc in self.khoaHoc:
                print(khoaHoc.thongTinKhoaHoc())
        else:
            print("Học viên chưa đăng ký khóa học nào.")


class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Khóa học: {self.tenKhoaHoc} - Hình thức: {self.hinhThuc} - Học phí: {self.hocPhi}"


# Học viên và Khóa học
hoc_vien1 = HocVien("HV001", "Nguyễn Ngọc Bảo châu", "01/01/1999")
hoc_vien2 = HocVien("HV002", "Trần Thị Ánh Tuyết", "05/05/1998")

khoa_hoc1 = KhoaHoc("KH001", "Lập trình Python", "Offline", 5000000)
khoa_hoc2 = KhoaHoc("KH002", "Machine Learning", "Online", 3000000)

# Đăng ký khóa học cho học viên
hoc_vien1.dangKyKhoaHoc(khoa_hoc1)
hoc_vien1.dangKyKhoaHoc(khoa_hoc2)
hoc_vien2.dangKyKhoaHoc(khoa_hoc2)

# Hiển thị thông tin khóa học của học viên
hoc_vien1.hienThiKhoaHoc()
hoc_vien2.hienThiKhoaHoc()
