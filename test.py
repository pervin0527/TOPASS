class Node:
    def __init__(self, data=None):
        self.prev = None
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.num_nodes = 0
        
        self.cursor = self.head  # 초기 커서를 head로 설정
        self.result = []

    def insert(self, data):
        new_node = Node(data)

        prev_node = self.tail.prev
        next_node = self.tail

        new_node.prev = prev_node
        new_node.next = next_node

        prev_node.next = new_node
        next_node.prev = new_node
        self.num_nodes += 1

    def delete(self, k):
        # 커서를 k-1번 만큼 앞으로 이동
        for _ in range(k):
            self.cursor = self.cursor.next
            if self.cursor == self.tail:
                self.cursor = self.head.next  # tail에서 벗어나지 않도록 조정

        # 커서가 가리키는 노드를 삭제
        curr_node = self.cursor
        prev_node = curr_node.prev
        next_node = curr_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.cursor = next_node
        if self.cursor == self.tail:
            self.cursor = self.head.next  # 다시 head의 다음 노드로 이동

        self.num_nodes -= 1
        self.result.append(curr_node.data)

    def __repr__(self) -> str:
        return f"<{', '.join(map(str, self.result))}>"
    
def solution():
    N, K = map(int, input().strip().split())
    ll = LinkedList()

    for i in range(1, N + 1):
        ll.insert(i)
    
    while ll.num_nodes > 0:
        ll.delete(K)

    print(ll)

if __name__ == "__main__":
    solution()
