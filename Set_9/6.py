class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def visit(node):
    print(node.data)


def traverse_preorder(top, visit):
    if top is None:
        return
    visit(top)
    traverse_preorder(top.left, visit)
    traverse_preorder(top.right, visit)


def traverse_inorder(top, visit):
    if top is None:
        return
    traverse_inorder(top.left, visit)
    visit(top)
    traverse_inorder(top.right, visit)


def traverse_postorder(top, visit):
    if top is None:
        return
    traverse_postorder(top.left, visit)
    traverse_postorder(top.right, visit)
    visit(top)


def traverse_stack(top, visit):
    if top is None:
        return
    stack = list()   # stos symulujemy przez listę Pythona
    stack.append(top)
    while stack:
        node = stack.pop()
        visit(node)   # przetworzenie node po zdjęciu ze stosu
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def btree_count(top):
    if top is None:
        return 0
    return btree_count(top.left) + 1 + btree_count(top.right)


def count_leafs(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    else:
        return count_leafs(top.left) + count_leafs(top.right)


def count_total(top):
    if top is None:
        return 0
    return count_total(top.left) + top.data + count_total(top.right)


root = None           # puste drzewo
root = Node("alone")  # drzewo z jednym węzłem
# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


traverse_preorder(root, visit)
x = btree_count(root)
print(f"/btree_count/{x}")

x = count_leafs(root)
print(f"/count_leafs/{x}")


x = count_total(root)
print(f"/count_total/{x}")
