import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("CyberSoft")
root.geometry("800x500")


frame_parent = customtkinter.CTkFrame(master=root)
frame_parent.place(relwidth=1, relheight=1)

colors = ["red", "green", "blue", "yellow"]
for i, color in enumerate(colors):
    frame = customtkinter.CTkFrame(master=frame_parent, fg_color=color)
    frame.place(relwidth=0.5, relheight=0.5, relx=(i % 2) * 0.5, rely=(i // 2) * 0.5)

root.mainloop()
