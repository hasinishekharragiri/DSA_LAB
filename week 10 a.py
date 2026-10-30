
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    return root.height if root else 0

def balance(root):
    return height(root.left) - height(root.right) if root else 0

def right_rotate(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def left_rotate(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and data < root.left.data:
        return right_rotate(root)
    if b < -1 and data > root.right.data:
        return left_rotate(root)
    if b > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if b < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def find_min(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.data

def find_max(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.data

def search(root, key):
    if not root or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    if not root:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return right_rotate(root)
    if b > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if b < -1 and balance(root.right) <= 0:
        return left_rotate(root)
    if b < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

root = None

while True:
    print("\n\n1.Insert 2.Inorder 3.Preorder")
    print("4.Postorder 5.Find Min 6.Find Max")
    print("7.Search 8.Delete 9.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        inorder(root)
    elif ch == 3:
        preorder(root)
    elif ch == 4:
        postorder(root)
    elif ch == 5:
        print("Minimum:", find_min(root))
    elif ch == 6:
        print("Maximum:", find_max(root))
    elif ch == 7:
        x = int(input("Enter value to search: "))
        print("Found" if search(root, x) else "Not Found")
    elif ch == 8:
        x = int(input("Enter value to delete: "))
        root = delete(root, x)
    elif ch == 9:
        break
    else:
        print("Invalid choice")

# Name: R. Hasinishekhar
# Roll No: 25146
