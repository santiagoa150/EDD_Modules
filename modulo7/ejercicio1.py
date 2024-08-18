class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    def preorder(self):
        elements = []
        self._preorder_recursively(self.root, elements)
        return elements

    def _preorder_recursively(self, root, elements):
        if root:
            elements.append(root.key)
            self._preorder_recursively(root.left, elements)
            self._preorder_recursively(root.right, elements)


for _ in range(int(input())):
    bt = BinarySearchTree()
    for i in tuple(map(int, input().split()))[:-1]:
        if i != -1:
            bt.insert(i)
    print(''.join(map(str, bt.preorder())))
