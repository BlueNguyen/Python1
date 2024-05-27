# import customtkinter as ctk

# class App(ctk.CTk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Thiết lập cửa sổ chính
#         self.title("CyberSoft")
#         self.geometry("500x500")

#         # Tạo một frame chính để chứa canvas và scrollbar
#         main_frame = ctk.CTkFrame(master=self)
#         main_frame.pack(fill="both", expand=True)

#         # Tạo canvas để chứa các nút
#         self.canvas = ctk.CTkCanvas(main_frame)
#         self.canvas.pack(side="left", fill="both", expand=True)

#         # Tạo scrollbar và liên kết nó với canvas
#         scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=self.canvas.yview)
#         scrollbar.pack(side="right", fill="y")

#         self.canvas.configure(yscrollcommand=scrollbar.set)

#         # Tạo một frame khác để chứa các nút và thêm nó vào canvas
#         self.button_frame = ctk.CTkFrame(master=self.canvas)
#         self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

#         # Tạo các nút
#         self.create_buttons()

#         # Đảm bảo canvas và nội dung của nó thay đổi kích thước đúng cách
#         self.button_frame.bind("<Configure>", self.on_configure)
#         self.button_frame.update_idletasks()

#     def button_command(self, index):
#         print(f"Button {index} clicked")

#     def create_buttons(self):
#         # Tạo 100 nút và thêm chúng vào frame
#         for i in range(100):
#             button = ctk.CTkButton(master=self.button_frame, text=f"Button {i+1}", command=lambda i=i: self.button_command(i+1))
#             button.pack(fill="x", pady=5, padx=5)

#     def on_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         # Đặt lại chiều rộng của button_frame để phù hợp với canvas
#         self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw"), width=self.canvas.winfo_width())

# if __name__ == "__main__":
#     ctk.set_default_color_theme("green")
#     ctk.set_appearance_mode("system")
    
#     app = App()
#     app.mainloop()


import customtkinter

class FrameGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, fg_color):
        super().__init__(master=master, fg_color=fg_color)
        self.grid(row=0, column=0, sticky="news")

        for index in range(1,100):
            button = customtkinter.CTkButton(self, text=f"Button {index} !", command= lambda index=index : self.button_event(index),fg_color="green")

            button.pack(fill="x", pady=10, padx=10)  # Sử dụng fill="x" và padx để chiếm toàn bộ chiều rộng

    def button_event(self,index):
        print(f"Button {index}")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CyberSoft")
        self.geometry("500x500")

        FrameGrid(self, "black")


app = App()

for column in range(0, 1):
    app.columnconfigure(column, weight=1)
    app.rowconfigure(column, weight=1)
app.mainloop()



