import customtkinter as ctk
from tkinter import simpledialog, messagebox

# Trie Implementation
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
    
    def censor(self, text):
        node = self.root
        i = 0
        start = 0
        result = []
        while i < len(text):
            if text[i] in node.children:
                node = node.children[text[i]]
                if node.is_end_of_word:
                    result.append('*' * (i - start + 1))
                    node = self.root
                    start = i + 1
                i += 1
            else:
                result.append(text[start])
                start += 1
                i = start
                node = self.root
        result.append(text[start:])
        return ''.join(result)

#UI 
class CensorApp:
    def __init__(self, root):
        self.root = root
        self.trie = Trie()
        self.sensitive_words = set()
        
        self.root.title("Fillter Char")
        
        self.messages_frame = ctk.CTkFrame(root, width=600, height=400)
        self.messages_frame.pack(pady=10)

        self.scrollbar = ctk.CTkScrollbar(self.messages_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.message_list = ctk.CTkTextbox(self.messages_frame, height=20, width=580, yscrollcommand=self.scrollbar.set, state="disabled")
        self.message_list.pack(side="left", fill="both", pady=10)
        
        self.scrollbar.configure(command=self.message_list.yview)
        
        self.entry_frame = ctk.CTkFrame(root, width=600, height=50)
        self.entry_frame.pack(pady=10)
        
        self.text_entry = ctk.CTkEntry(self.entry_frame, width=500)
        self.text_entry.pack(side="left", padx=10)
        
        self.censor_button = ctk.CTkButton(self.entry_frame, text="Gửi", command=self.censor_text)
        self.censor_button.pack(side="left")
        
        self.add_word_button = ctk.CTkButton(root, text="Thêm vào danh sách từ nhạy cảm", command=self.add_sensitive_word)
        self.add_word_button.pack(pady=5)
        
        self.remove_word_button = ctk.CTkButton(root, text="Xoá khỏi danh sách", command=self.remove_sensitive_word)
        self.remove_word_button.pack(pady=5)
    
    def censor_text(self):
        text = self.text_entry.get()
        if text:
            result = self.trie.censor(text)
            self.message_list.configure(state="normal")
            self.message_list.insert("end", f"{result}\n", "user_message")
            self.message_list.configure(state="disabled")
            self.message_list.yview("end")
            self.text_entry.delete(0, "end")
    
    def add_sensitive_word(self):
        word = simpledialog.askstring("Input", "Nhập từ muốn thêm:")
        if word:
            self.trie.insert(word)
            self.sensitive_words.add(word)
            messagebox.showinfo("Info", f"'{word}' đã được thêm vào danh sách.")
    
    def remove_sensitive_word(self):
        word = simpledialog.askstring("Input", "Nhập từ muốn xoá:")
        if word and word in self.sensitive_words:
            self.sensitive_words.remove(word)
            self.rebuild_trie()
            messagebox.showinfo("Info", f"'{word}' đã được xoá khỏi danh sách.")
    
    def rebuild_trie(self):
        self.trie = Trie()
        for word in self.sensitive_words:
            self.trie.insert(word)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
    
    root = ctk.CTk()
    app = CensorApp(root)
    root.mainloop()
