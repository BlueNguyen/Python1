class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def build_bst(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    for value in arr[1:]:
        insert(root, value)
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

# Hàm để in ra cây dưới dạng đồ họa (optional)
def print_bst(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level*4) + prefix + str(root.value))
        if root.left:
            print_bst(root.left, level + 1, "L--- ")
        if root.right:
            print_bst(root.right, level + 1, "R--- ")

# Ví dụ sử dụng
prices = [13, 20, 4, 2, 14, 22, 5]
bst_root = build_bst(prices)

print("In-order Traversal của BST:", inorder_traversal(bst_root))
print("\nCấu trúc cây BST:")
print_bst(bst_root)
