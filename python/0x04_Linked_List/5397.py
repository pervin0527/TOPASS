import sys

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
        self.cursor = self.tail

    def insert(self, data):
        new_node = Node(data)

        prev_node = self.cursor.prev
        next_node = self.cursor

        new_node.prev = prev_node
        new_node.next = next_node

        prev_node.next = new_node
        next_node.prev = new_node

    def delete(self):
        target_node = self.cursor.prev
        if target_node != self.head:
            prev_node = target_node.prev
            next_node = target_node.next

            prev_node.next = next_node
            next_node.prev = prev_node

    def move_left(self):
        if self.cursor.prev != self.head: ## 커서는 head가 될 수 없다. 즉, 연결리스트의 첫번째 원소가 왼쪽으로 이동할 수 있는 마지막임.
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def __repr__(self) -> str:
        result = ""
        curr_node = self.head.next
        while curr_node != self.tail:
            result += f"{curr_node.data}"
            curr_node = curr_node.next

        return result


def solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        ll = LinkedList()
        line = sys.stdin.readline().strip()

        for l in line:
            if l == "<":
                ll.move_left()
            elif l == ">":
                ll.move_right()
            elif l == "-":
                ll.delete()
            else:
                ll.insert(l)

        print(ll)


if __name__ == "__main__":
    solution()