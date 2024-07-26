class TreeNode:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, price, name):
        new_node = TreeNode(price, name)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.price < current.price:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left, result)
            result.append((current.name, current.price))
            self._inorder_recursive(current.right, result)

    def print_bst(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + f"{node.name} ({node.price})")
            if node.left:
                self.print_bst(node.left, level + 1, "L--- ")
            if node.right:
                self.print_bst(node.right, level + 1, "R--- ")

# Dữ liệu iPhone từ hình ảnh
iphones = [
    {"price": 3000, "name": "iphone12"},
    {"price": 1000, "name": "iphone10"},
    {"price": 5000, "name": "iphone14"},
    {"price": 2000, "name": "iphone11"},
    {"price": 4000, "name": "iphone13"}
]

# Tạo đối tượng BST và chèn dữ liệu iPhone vào cây
bst = BST()
for iphone in iphones:
    bst.insert(iphone["price"], iphone["name"])

# Duyệt cây in-order và in ra kết quả
print("In-order Traversal của BST:")
for name, price in bst.inorder_traversal():
    print(f"{name} ({price})")

# In ra cấu trúc cây BST
print("\nCấu trúc cây BST:")
bst.print_bst()
