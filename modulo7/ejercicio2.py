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

    def get_height(self):
        if self.root:
            return self._get_height_recursively(self.root, 1)
        return 0

    def _get_height_recursively(self, root, height):
        left, right = 0, 0
        if root is None:
            return height
        new = height + 1
        if root.left is not None or root.right is not None:
            if root.left is not None:
                left = self._get_height_recursively(root.left, new)
            if root.right is not None:
                right = self._get_height_recursively(root.right, new)
        else:
            return height
        return max([left, right])


for _ in range(int(input())):
    bt = BinarySearchTree()
    for i in tuple(map(int, input().split()))[:-1]:
        if i != -1:
            bt.insert(i)
    print(bt.get_height())
