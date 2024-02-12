class Node:
    def __init__(self, data=None):
        self.next, self.prev = None, None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.num_nodes = 0

        self.cursor = self.tail
        self.arr = []

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev

        self.cursor.prev.next = new_node
        self.cursor.prev = new_node

        self.num_nodes += 1

    def move_right(self):
        if self.cursor.next == self.tail: ## 현재 노드의 다음이 tail인 경우, 마지막 노드이므로 첫번째 노드로 커서를 이동.
            self.cursor = self.head.next
        else: ## 아닌 경우, 커서를 오른쪽으로 한 칸 이동.
            self.cursor = self.cursor.next

    def process(self, k):
        result = []
        self.cursor = self.head.next
        while self.num_nodes > 0:
            for _ in range(k-1):
                self.move_right()

            result.append(self.cursor.data) ## 현재 노드(삭제 대상)의 값 저장.
            
            next_node = self.cursor.next ## 현재 노드의 이전 노드
            prev_node = self.cursor.prev ## 현재 노드의 다음 노드
            
            ## 노드 삭제.
            next_node.prev = prev_node
            prev_node.next = next_node
            self.num_nodes -= 1

            ## 삭제 후 커서를 한 칸 이동.
            self.move_right()

        return result
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    ll = LinkedList()

    for i in range(1, n+1):
        ll.insert(i)

    result = ll.process(k)
    result = ", ".join([str(x) for x in result])
    print(f"<{result}>")