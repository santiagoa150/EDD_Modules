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

    def count_only_child(self):
        return self._count_only_child_recursively(self.root)

    def _count_only_child_recursively(self, root):
        if root is None:
            return 0
        elif root.left is not None and root.right is None:
            return 1 + self._count_only_child_recursively(root.left)
        elif root.right is not None and root.left is None:
            return 1 + self._count_only_child_recursively(root.right)
        else:
            return self._count_only_child_recursively(root.left) + self._count_only_child_recursively(root.right)


for _ in range(int(input())):
    bt = BinarySearchTree()
    for i in tuple(map(int, input().split()))[:-1]:
        if i != -1:
            bt.insert(i)
    print(bt.count_only_child())
