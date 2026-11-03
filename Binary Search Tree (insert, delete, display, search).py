class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def min_node(root):
    while root.left:
        root = root.left
    return root

def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        s = min_node(root.right)
        root.key = s.key
        root.right = delete(root.right, s.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None
for k in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, k)

print("Inorder:", end=" ")
inorder(root)
print()

print("Search 60:", "Found" if search(root, 60) else "Not found")
print("Search 90:", "Found" if search(root, 90) else "Not found")

for k in [20, 30, 50]:
    root = delete(root, k)
    print("After deleting", k, ":", end=" ")
    inorder(root)
    print()