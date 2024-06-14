import customtkinter as ctk
from tkinter import simpledialog, messagebox

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def censor_text(self, text):
        words = text.split()
        for i, word in enumerate(words):
            if self.search(word):
                words[i] = '*' * len(word)
        return ' '.join(words)

class CensorshipApp:
    def __init__(self, root):
        self.trie = Trie()
        self.root = root
        self.root.title("Filter Char")
        self.root.geometry("800x600")
        
        self.input_label = ctk.CTkLabel(root, text="Nhập văn bản:")
        self.input_label.pack(pady=50)

        self.text_area = ctk.CTkTextbox(root, height=10, width=50)
        self.text_area.pack(pady=50)

        self.censor_button = ctk.CTkButton(root, text="Lọc từ nhạy cảm", command=self.censor_text)
        self.censor_button.pack(pady=10)

        self.original_label = ctk.CTkLabel(root, text="Văn bản gốc:")
        self.original_label.pack(pady=10)

        self.original_area = ctk.CTkTextbox(root, height=10, width=50, state='disabled')
        self.original_area.pack(pady=10)

        self.result_label = ctk.CTkLabel(root, text="Kết quả sau khi lọc:")
        self.result_label.pack(pady=10)

        self.result_area = ctk.CTkTextbox(root, height=10, width=50, state='disabled')
        self.result_area.pack(pady=10)

        self.add_word_button = ctk.CTkButton(root, text="Thêm từ nhạy cảm", command=self.add_sensitive_word)
        self.add_word_button.pack(pady=10)

    def censor_text(self):
        text = self.text_area.get("1.0", "end-1c").strip()
        censored_text = self.trie.censor_text(text)
        
        self.original_area.configure(state='normal')
        self.original_area.delete("1.0", "end")
        self.original_area.insert("end", text)
        self.original_area.configure(state='disabled')
        
        self.result_area.configure(state='normal')
        self.result_area.delete("1.0", "end")
        self.result_area.insert("end", censored_text)
        self.result_area.configure(state='disabled')

    def add_sensitive_word(self):
        word = simpledialog.askstring("Thêm từ nhạy cảm", "Nhập từ nhạy cảm:")
        if word:
            self.trie.insert(word)
            messagebox.showinfo("Thông báo", f"Đã thêm từ '{word}' vào danh sách từ nhạy cảm.")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Bạn có thể chuyển thành "light" nếu muốn
    ctk.set_default_color_theme("blue")  # Bạn có thể chọn màu khác như "green" hoặc "dark-blue"

    root = ctk.CTk()
    app = CensorshipApp(root)
    root.mainloop()
