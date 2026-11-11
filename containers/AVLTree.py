'''
This file implements the AVL Tree data structure.
'''

import copy

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    AVLTree is a subclass of BST with automatic rebalancing.
    '''

    def __init__(self, xs=None):
        super().__init__()
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if node is None:
            return True
        if abs(AVLTree._balance_factor(node)) > 1:
            return False
        return AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        if node is None or node.right is None:
            return node
        new_root = copy.copy(node.right)
        new_node = copy.copy(node)
        new_node.right = new_root.left
        new_root.left = new_node
        return new_root

    @staticmethod
    def _right_rotate(node):
        if node is None or node.left is None:
            return node
        new_root = copy.copy(node.left)
        new_node = copy.copy(node)
        new_node.left = new_root.right
        new_root.right = new_node
        return new_root

    def insert(self, value):
        self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        elif value > node.value:
            node.right = AVLTree._insert(node.right, value)
        else:
            return node
        return AVLTree._rebalance(node)

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    @staticmethod
    def _rebalance(node):
        if node is None:
            return node
        bf = AVLTree._balance_factor(node)
        if bf > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        if bf < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)
        return node
