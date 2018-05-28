# Module with class representing a node of binary tree
class Node:

    def __init__(self, tree, item, parent=None):
        """Create instance of binary tree node"""
        self.tree = tree
        self.item = item
        self.parent = parent
        self.score = None
        self.children = []

    def is_root(self):
        """Check if node is a root"""
        return self.parent is None

    def is_leaf(self):
        """Check if node is a leaf"""
        return self.children == []
