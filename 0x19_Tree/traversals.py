class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order_traversal(node):
    if node:
        print(node.val, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=' ')
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=' ')