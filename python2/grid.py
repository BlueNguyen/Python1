import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("CyberSoft")
root.geometry("800x500")

frame_parent = customtkinter.CTkFrame(master=root)
frame_parent.pack(fill="both", expand=True)

colors = ["yellow", "red", "grey", "blue"]

# Cấu hình cột và hàng trước khi thêm các frame con
for i in range(2):  # Giả sử chúng ta chỉ có 2 cột
    frame_parent.grid_columnconfigure(i, weight=1)
for i in range(2):  # Giả sử chúng ta chỉ có 2 hàng
    frame_parent.grid_rowconfigure(i, weight=1)

for i, color in enumerate(colors):
    # Tính toán vị trí row và column
    # Vị trí hàng được tính bằng cách chia chỉ số i cho 2 và lấy phần nguyên
    # Vị trí cột được tính bằng cách lấy phần dư của chỉ số i khi chia cho 2
    row = i // 2
    column = i % 2

    frame = customtkinter.CTkFrame(master=frame_parent, fg_color=color)
    frame.grid(row=row, column=column, sticky="nsew")

root.mainloop()
