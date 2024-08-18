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

    def count_elements_by_level(self):
        levels = {}
        if self.root:
            self._count_elements_by_level_recursively(self.root, 0, levels)
        return levels

    def _count_elements_by_level_recursively(self, root, current_level, levels):
        try:
            levels[current_level] += 1
        except:
            levels[current_level] = 1

        if root.left is not None:
            self._count_elements_by_level_recursively(root.left, current_level + 1, levels)
        if root.right is not None:
            self._count_elements_by_level_recursively(root.right, current_level + 1, levels)


for _ in range(int(input())):
    bt = BinarySearchTree()
    for i in tuple(map(int, input().split()))[:-1]:
        if i != -1:
            bt.insert(i)
    levels = bt.count_elements_by_level()
    is_real = True
    for level in levels.items():
        if level[1] != (2 ** level[0]):
            is_real = False
            break

    if is_real:
        print('completo')
    else:
        print('no')
