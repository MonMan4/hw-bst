'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit* vector implementation,
so the code in the book is likely to be less helpful than the code for the other data structures.
The book's implementation is the traditional implementation because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help you get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        self.size = 0
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        if node is None:
            return True
        if node.left is not None and node.left.value < node.value:
            return False
        if node.right is not None and node.right.value < node.value:
            return False
        return Heap._is_heap_satisfied(node.left) and Heap._is_heap_satisfied(node.right)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size = 1
            return
        self.size += 1
        path = bin(self.size)[3:]
        Heap._insert_at(self.root, path, value)

    @staticmethod
    def _insert_at(node, path, value):
        if len(path) == 1:
            if path == '0':
                node.left = Node(value)
                if node.left.value < node.value:
                    node.value, node.left.value = node.left.value, node.value
            else:
                node.right = Node(value)
                if node.right.value < node.value:
                    node.value, node.right.value = node.right.value, node.value
            return
        if path[0] == '0':
            Heap._insert_at(node.left, path[1:], value)
            if node.left.value < node.value:
                node.value, node.left.value = node.left.value, node.value
        else:
            Heap._insert_at(node.right, path[1:], value)
            if node.right.value < node.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        if self.root is None:
            return None
        return self.root.value

    def remove_min(self):
        if self.root is None:
            return
        if self.size == 1:
            self.root = None
            self.size = 0
            return
        path = bin(self.size)[3:]
        br_value = Heap._remove_bottom_right(self.root, path)
        self.root.value = br_value
        self.size -= 1
        Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, path):
        if len(path) == 1:
            if path == '0':
                v = node.left.value
                node.left = None
                return v
            else:
                v = node.right.value
                node.right = None
                return v
        if path[0] == '0':
            return Heap._remove_bottom_right(node.left, path[1:])
        else:
            return Heap._remove_bottom_right(node.right, path[1:])

    @staticmethod
    def _trickle(node):
        if node is None:
            return
        smallest = node
        if node.left is not None and node.left.value < smallest.value:
            smallest = node.left
        if node.right is not None and node.right.value < smallest.value:
            smallest = node.right
        if smallest is not node:
            node.value, smallest.value = smallest.value, node.value
            Heap._trickle(smallest)
