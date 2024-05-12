import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("CyberSoft")
root.geometry("800x500")

# Row Top
frameTop = customtkinter.CTkFrame(master=root, fg_color="black")
frameTop.pack(fill="both", expand=True, side="top")

frameLeft1 = customtkinter.CTkFrame(master=frameTop, fg_color="blue")
frameLeft1.pack(fill="both", expand=True, side="left")

frameRight1 = customtkinter.CTkFrame(master=frameTop, fg_color="yellow")
frameRight1.pack(fill="both", expand=True, side="right")

# Row Bottom
frameBot = customtkinter.CTkFrame(master=root, fg_color="black")
frameBot.pack(fill="both", expand=True, side="bottom")

frameLeft1 = customtkinter.CTkFrame(master=frameBot, fg_color="green")
frameLeft1.pack(fill="both", expand=True, side="left")

frameRight1 = customtkinter.CTkFrame(master=frameBot, fg_color="red")
frameRight1.pack(fill="both", expand=True, side="right")

root.mainloop()
