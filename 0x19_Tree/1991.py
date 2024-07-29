import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.value, end='')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end='')
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end='')

def solution():
    num_nodes = int(input().strip())
    
    tree = {}
    for _ in range(num_nodes):
        p, lc, rc = input().strip().split()

        if p not in tree:
            tree[p] = TreeNode(p)
        if lc != ".":
            tree[lc] = TreeNode(lc)
            tree[p].left = tree[lc]
        if rc != '.':
            tree[rc] = TreeNode(rc)
            tree[p].right = tree[rc]
    
    root = tree['A']
    preorder_traversal(root)
    print()

    inorder_traversal(root)
    print()

    postorder_traversal(root)
    print()

if __name__ == "__main__":
    solution()