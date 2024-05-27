import customtkinter as ctk

# Thiết lập chủ đề và chế độ giao diện
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("system")

# Cửa sổ chính
root = ctk.CTk()
root.title("CyberSoft")
root.geometry("500x500")

# Tạo một frame chính để chứa canvas và scrollbar
main_frame = ctk.CTkFrame(master=root)
main_frame.pack(fill="both", expand=True)

# Tạo canvas để chứa các nút
canvas = ctk.CTkCanvas(main_frame)
canvas.pack(side="left", fill="both", expand=True)

# Tạo scrollbar và liên kết nó với canvas
scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Tạo một frame khác để chứa các nút và thêm nó vào canvas
button_frame = ctk.CTkFrame(master=canvas)

# Đặt frame này trong canvas
canvas.create_window((0, 0), window=button_frame, anchor="nw")

# Hàm để in chỉ số của nút khi bấm vào
def button_command(index):
    print(f"Button {index} clicked")

# Tạo 100 nút và thêm chúng vào frame
for i in range(100):
    button = ctk.CTkButton(master=button_frame, text=f"Button {i+1}", command=lambda i=i: button_command(i+1))
    button.pack(fill="x", pady=5, padx=5)

# Cập nhật vùng cuộn
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    # Đặt lại chiều rộng của button_frame để phù hợp với canvas
    canvas.itemconfig(canvas.create_window((0, 0), window=button_frame, anchor="nw"), width=canvas.winfo_width())

button_frame.bind("<Configure>", on_configure)

# Đảm bảo canvas và nội dung của nó thay đổi kích thước đúng cách
button_frame.update_idletasks()

# Chạy vòng lặp chính
root.mainloop()
