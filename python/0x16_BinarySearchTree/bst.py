class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp_val = self._min_value_node(node.right).val
            node.val = temp_val
            node.right = self._delete(node.right, temp_val)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)

# 사용 예제
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("이진 검색 트리의 중위 순회 결과:")
bst.inorder()

print("노드 40 검색 결과:", bst.search(40))
print("노드 90 검색 결과:", bst.search(90))

bst.delete(20)
print("노드 20 삭제 후 중위 순회 결과:")
bst.inorder()

bst.delete(30)
print("노드 30 삭제 후 중위 순회 결과:")
bst.inorder()

bst.delete(50)
print("노드 50 삭제 후 중위 순회 결과:")
bst.inorder()
