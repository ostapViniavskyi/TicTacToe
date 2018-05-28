# Module with class representing a binary tree
from btnode import Node


class Tree:

    def __init__(self):
        """Create instance of BinaryTree"""
        self._root = None

    def is_empty(self):
        """Check if tree is empty"""
        return self._root is None

    def add_root(self, item):
        """Add root to the tree"""
        root = Node(self, item)
        self._root = root
        return root

    def add_child(self, node, item):
        """Add child to the node"""
        if node.tree is not self:
            raise ValueError('Node does not belong to a tree!!!')
        child = Node(self, item, node)
        node.children.append(child)
        return child
