import customtkinter

# Thiết lập chủ đề và chế độ giao diện
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

# Cửa sổ chính
root = customtkinter.CTk()
root.title("CyberSoft")  
root.geometry("500x300")  
root.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

# Chạy vòng lặp chính
root.mainloop()
