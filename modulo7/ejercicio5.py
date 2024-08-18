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

    def print_tree(self):
        self._print_tree_recursively(self.root, 0)
        print('')

    def _print_tree_recursively(self, root, level):
        if root.right is not None:
            self._print_tree_recursively(root.right, level + 1)
        print(''.join(['\t\t' for _ in range(level)]), root.key, sep='')
        if root.left is not None:
            self._print_tree_recursively(root.left, level + 1)


for _ in range(int(input())):
    bt = BinarySearchTree()
    for i in tuple(map(int, input().split()))[:-1]:
        if i != -1:
            bt.insert(i)
    bt.print_tree()
