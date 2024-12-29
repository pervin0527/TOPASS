from __future__ import annotations ## type hint

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child : TreeNode) -> None:
        """
        특정 노드에 자식 노드를 추가한다. 자식 노드의 parent는 부모 노드를 추가.
        """
        self.children.append(child)
        child.parent = self

    def get_level(self):
        """
        특정 노드에서 시작해 부모 노드 방향으로 올라간다.
        """
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level 

class Tree:
    def __init__(self):
        self.root = None ## 루트 노드
        self.height = 0 ## 트리의 높이
        self.nodes = [] ## 트리에 포함되는 노드 리스트

    def insert(self, node, parent):
        """
        트리에서 특정 부모 노드에 자식 노드를 추가한다.
        parent가 None이면 루트 노드가 트리에 삽입될 때.
        """
        if parent is not None: ## 부모 노드가 트리에 존재하면 자식 노드로 추가
            parent.add_child(node)

        else: ## 부모 노드가 존재하지 않으면(None) 부모 노드를 트리에 추가. 이 경우 루트 노드를 트리에 삽입하는 것이다.
            if self.root is None:
                self.root=node

        self.nodes.append(node)