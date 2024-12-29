class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.num_nodes = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def traverse(self):
        curr_node = self.head.next
        while curr_node != self.tail:
            print(curr_node.item)
            curr_node = curr_node.next

    def insert(self, idx, item):
        if idx < 0 or idx > self.num_nodes:
            return False

        new_node = Node(item)
        curr_node = self.head
        for _ in range(idx):  # 0부터 시작하므로 idx까지 이동
            curr_node = curr_node.next

        next_node = curr_node.next

        curr_node.next = new_node
        new_node.prev = curr_node
        new_node.next = next_node
        next_node.prev = new_node

        self.num_nodes += 1
        return True

    def pop(self, idx):
        if idx < 0 or idx >= self.num_nodes:
            return False

        curr_node = self.head.next
        for _ in range(idx):  # 0부터 시작하므로 idx까지 이동
            curr_node = curr_node.next

        prev_node = curr_node.prev
        next_node = curr_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.num_nodes -= 1
        return curr_node.item

    def search(self, item):
        curr_node = self.head.next
        idx = 0
        while curr_node != self.tail:
            if curr_node.item == item:
                return idx
            curr_node = curr_node.next
            idx += 1
        return -1

    def __repr__(self):
        items = []
        curr_node = self.head.next
        while curr_node != self.tail:
            items.append(curr_node.item)
            curr_node = curr_node.next
        return "DoublyLinkedList([" + ", ".join(map(str, items)) + "])"


# 테스트
ll = DoublyLinkedList()
ll.insert(0, 10)
ll.insert(1, 20)
ll.insert(1, 15)
ll.traverse()  # 10 15 20 출력
print(ll)  # DoublyLinkedList([10, 15, 20]) 출력
print("Pop:", ll.pop(1))  # Pop: 15 출력
print(ll)  # DoublyLinkedList([10, 20]) 출력
print("Search 20:", ll.search(20))  # Search 20: 1 출력
print("Search 30:", ll.search(30))  # Search 30: -1 출력
