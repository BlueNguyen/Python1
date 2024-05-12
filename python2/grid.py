import customtkinter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("system")

root = customtkinter.CTk()
root.title("CyberSoft")
root.geometry("800x500")

frame_parent = customtkinter.CTkFrame(master=root)
frame_parent.pack(fill="both", expand=True)

colors = ["red", "green", "blue", "yellow"]
for i, color in enumerate(colors):
    frame = customtkinter.CTkFrame(master=frame_parent, fg_color=color)
    frame.grid(row=i//2, column=i%2, sticky="nsew")
    
    frame_parent.grid_columnconfigure(i%2, weight=1)
    frame_parent.grid_rowconfigure(i//2, weight=1)

root.mainloop()
