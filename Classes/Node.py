class Node:
    def __init__(self, word, color, parent, left, right):
        self.word = word
        self.color = color
        self.parent = parent
        self.right = None
        self.left = None

    def __repr__(self):
        return self.word + "(" + self.color + ")"

    def in_order_traversal(self):
        if self is None:
            return
        self.in_order_traversal(self.left)
        print(self)
        self.in_order_traversal(self.right)

    def children(self):
        if (self.right is None) and (self.left is None):
            return 0
        elif (self.right is not None) and (self.left is not None):
            return 1
        else:
            return 2

