class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))

        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height

    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)

    def get_ring(self):
        ring = []
        elements = []
        root_child = AVLTree.get_child_num(self.root)
        ring.append(root_child)
        if root_child == 2:
            elements.append(self.root.left)
            elements.append(self.root.right)
            ring.append(AVLTree.get_child_num(self.root.left))
            ring.append(AVLTree.get_child_num(self.root.right))
        elif root_child == -1:
            elements.append(self.root.left)
            ring.append(AVLTree.get_child_num(self.root.left))
        elif root_child == 1:
            elements.append(self.root.right)
            ring.append(AVLTree.get_child_num(self.root.right))
        self._get_ring_recursively(ring, elements)
        return ring

    @staticmethod
    def get_child_num(root):
        if root:
            if root.left is not None and root.right is not None:
                return 2
            if root.left is not None:
                return -1
            if root.right is not None:
                return 1
            return 0

    def _get_ring_recursively(self, ring, elements):
        if len(elements) > 0:
            next_elements = []
            for root in elements:
                if root.left is not None:
                    ring.append(AVLTree.get_child_num(root.left))
                    next_elements.append(root.left)
                if root.right is not None:
                    ring.append(AVLTree.get_child_num(root.right))
                    next_elements.append(root.right)
            self._get_ring_recursively(ring, next_elements)


while True:
    n = int(input())
    if n == 0:
        break
    avl = AVLTree()
    for i in tuple(map(int, input().split())):
        avl.insert(i)
    print('.'.join(map(str, avl.get_ring())))
