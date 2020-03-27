class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 0

    def __str__(self):
        return str(self.key) + "(" + str(self.height) + ")"

    def is_leaf(self):
        return (self.height == 0)

    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.height, self.rightChild.height)
        elif self.leftChild and not self.rightChild:
            return self.leftChild.height
        elif not self.leftChild and self.rightChild:
            return self.rightChild.height
        else:
            return -1

    def balance(self):
        return (self.leftChild.height if self.leftChild else -1) - (self.rightChild.height if self.rightChild else -1)
class AVLTree():
    def __init__(self, *args):
        self.rootNode = None
        self.elements_count = 0
        self.rebalance_count = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert (i)

    def height(self):
        if self.rootNode:
            return self.rootNode.height
        else:
            return 0