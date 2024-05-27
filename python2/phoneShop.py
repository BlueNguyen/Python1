import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProductGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Danh sách sản phẩm iPhone")
        
        # Tạo thanh cuộn
        self.scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        
        # Tạo canvas để hiển thị danh sách sản phẩm
        self.canvas = tk.Canvas(self, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.canvas.yview)
        
        # Tạo frame con trong canvas để chứa danh sách sản phẩm
        self.product_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.product_frame, anchor="nw")
        
        # Load hình ảnh sản phẩm
        self.load_product_images()
        
    def load_product_images(self):
        # Danh sách tên hình ảnh sản phẩm
        product_images = ["iphone_11_pro_max.png", "iphone_12.png", "iphone_12_mini.png", "iphone_se_2020.png"]
        
        # Hiển thị hình ảnh sản phẩm trên mỗi hàng (4 sản phẩm trên một hàng)
        row = 0
        column = 0
        for i, image_name in enumerate(product_images):
            product_image = Image.open(image_name)
            product_photo = ImageTk.PhotoImage(product_image)
            
            # Hiển thị hình ảnh sản phẩm trên canvas
            label = tk.Label(self.product_frame, image=product_photo)
            label.image = product_photo  # Giữ tham chiếu đến hình ảnh để ngăn hình ảnh bị thu hồi
            label.grid(row=row, column=column, padx=10, pady=10)
            
            # Di chuyển đến hàng và cột tiếp theo
            column += 1
            if column == 4:  # 4 sản phẩm trên một hàng
                column = 0
                row += 1

if __name__ == "__main__":
    app = ProductGUI()
    app.mainloop()
