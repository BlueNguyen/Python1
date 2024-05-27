# import customtkinter

# customtkinter.set_default_color_theme("green")
# customtkinter.set_appearance_mode("system")

# root = customtkinter.CTk()
# root.title("CyberSoft")
# root.geometry("800x500")

# frame_parent = customtkinter.CTkFrame(master=root)
# frame_parent.pack(fill="both", expand=True)

# colors = ["yellow", "red", "grey", "blue"]

# # Cấu hình cột và hàng trước khi thêm các frame con
# for i in range(2):  # Giả sử chúng ta chỉ có 2 cột
#     frame_parent.grid_columnconfigure(i, weight=1)
# for i in range(2):  # Giả sử chúng ta chỉ có 2 hàng
#     frame_parent.grid_rowconfigure(i, weight=1)

# for i, color in enumerate(colors):
#     # Tính toán vị trí row và column
#     # Vị trí hàng được tính bằng cách chia chỉ số i cho 2 và lấy phần nguyên
#     # Vị trí cột được tính bằng cách lấy phần dư của chỉ số i khi chia cho 2
#     row = i // 2
#     column = i % 2

#     frame = customtkinter.CTkFrame(master=frame_parent, fg_color=color)
#     frame.grid(row=row, column=column, sticky="nsew")

# root.mainloop()


import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("CyberSoft")
root.geometry("800x500")

# Tạo khung cha 
frame_parent = customtkinter.CTkFrame(master=root)
frame_parent.pack(fill="both", expand=True)

# Cấu hình column và row trước khi thêm các frame con
frame_parent.grid_columnconfigure(0, weight=1)
frame_parent.grid_columnconfigure(1, weight=1)
frame_parent.grid_rowconfigure(0, weight=1)
frame_parent.grid_rowconfigure(1, weight=1)

# Đặt các frame vào grid
frameTopLeft = customtkinter.CTkFrame(master=frame_parent, fg_color="yellow")
frameTopLeft.grid(row=0, column=0, sticky="nsew")

frameTopRight = customtkinter.CTkFrame(master=frame_parent, fg_color="red")
frameTopRight.grid(row=0, column=1, sticky="nsew")

frameBotLeft = customtkinter.CTkFrame(master=frame_parent, fg_color="grey")
frameBotLeft.grid(row=1, column=0, sticky="nsew")

frameBotRight = customtkinter.CTkFrame(master=frame_parent, fg_color="blue")
frameBotRight.grid(row=1, column=1, sticky="nsew")

root.mainloop()
