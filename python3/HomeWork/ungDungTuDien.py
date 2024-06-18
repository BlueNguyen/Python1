import customtkinter as ctk
from tkinter import simpledialog, messagebox

# Trie Implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.meaning = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.meaning = meaning
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end_of_word:
            return node.meaning
        return None
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        result = []
        self._dfs(node, prefix, result)
        return result
    
    def _dfs(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, result)

class DictionaryApp:
    def __init__(self, root):
        self.root = root
        self.trie = Trie()
        
        self.root.title("Dictionary")
        
        self.left_frame = ctk.CTkFrame(root)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
        
        self.right_frame = ctk.CTkFrame(root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.word_list = ctk.CTkTextbox(self.left_frame, width=200, height=100)  # Adjust width and height
        self.word_list.pack(pady=10)
        
        self.search_entry = ctk.CTkEntry(self.right_frame)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.search_button = ctk.CTkButton(self.right_frame, text="Search", command=self.search_word)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.search_entry.bind("<KeyRelease>", self.autocomplete)
        
        self.result_listbox = ctk.CTkTextbox(self.right_frame, width=10, height=10)
        self.result_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.result_label = ctk.CTkLabel(self.right_frame, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.add_word_button = ctk.CTkButton(root, text="Add Word", command=self.add_word)
        self.add_word_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        self.edit_word_button = ctk.CTkButton(root, text="Edit Word", command=self.edit_word)
        self.edit_word_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    def search_word(self):
        word = self.search_entry.get().strip()
        meaning = self.trie.search(word)
        if meaning:
            self.result_label.configure(text=f"{word} (noun): {meaning}")
        else:
            self.result_label.configure(text=f"'{word}' not found in the dictionary.")
    
    def autocomplete(self, event):
        prefix = self.search_entry.get().strip()
        if prefix:
            words = self.trie.starts_with(prefix)
            self.result_listbox.configure(state="normal")
            self.result_listbox.delete("1.0", "end")
            for word in words:
                self.result_listbox.insert("end", word + "\n")
            self.result_listbox.configure(state="disabled")
        else:
            self.result_listbox.configure(state="normal")
            self.result_listbox.delete("1.0", "end")
            self.result_listbox.configure(state="disabled")
    
    def add_word(self):
        word = simpledialog.askstring("Input", "Enter the word:")
        meaning = simpledialog.askstring("Input", "Enter the meaning:")
        if word and meaning:
            self.trie.insert(word, meaning)
            self.update_word_list()
            messagebox.showinfo("Info", f"'{word}' added to the dictionary.")
    
    def edit_word(self):
        word = simpledialog.askstring("Input", "Enter the word to edit:")
        if word:
            meaning = self.trie.search(word)
            if meaning:
                new_meaning = simpledialog.askstring("Input", f"Current meaning: {meaning}\nEnter the new meaning:")
                if new_meaning:
                    self.trie.insert(word, new_meaning)
                    messagebox.showinfo("Info", f"'{word}' has been updated.")
            else:
                messagebox.showinfo("Info", f"'{word}' not found in the dictionary.")
    
    def update_word_list(self):
        words = self.trie.starts_with("")
        self.word_list.configure(state="normal")
        self.word_list.delete("1.0", "end")
        for word in words:
            self.word_list.insert("end", word + "\n")
        self.word_list.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
    
    root = ctk.CTk()
    app = DictionaryApp(root)
    root.mainloop()
