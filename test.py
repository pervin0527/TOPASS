import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = Node(None)  # 연결 리스트의 머리
        self.tail = Node(None)  # 연결 리스트의 꼬리
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail  # 초기 커서는 문자열의 끝을 가리킴

    def insert(self, char):
        node = Node(char)
        
        ## 커서의 왼쪽에 문자를 추가.
        node.prev = self.cursor.prev ## 새 노드의 prev 포인터를 커서의 현재 위치 바로 앞에 있는 노드(cursor.prev)로 설정.
        node.next = self.cursor ## 새 노드의 next 포인터를 현재 커서가 가리키는 노드로 설정.

        self.cursor.prev.next = node ## 커서 앞의 노드의 next 포인터를 새 노드로 설정.
        self.cursor.prev = node ## 커서의 prev 포인터를 새 노드로 설정.

    def delete(self):
        if self.cursor.prev != self.head:  # 삭제할 노드가 있으면, 커서 왼쪽에 있는 문자를 삭제.
            self.cursor.prev.prev.next = self.cursor ## 삭제할 노드(cursor.prev)의 이전 노드의 next 포인터를 커서가 가리키는 노드로 설정하여, 삭제할 노드를 연결 리스트에서 분리.
            self.cursor.prev = self.cursor.prev.prev ## 커서의 prev 포인터를 삭제할 노드의 이전 노드로 업데이트.

    def move_left(self):
        if self.cursor.prev != self.head:  # 커서가 맨 앞이 아니면
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:  # 커서가 맨 뒤가 아니면
            self.cursor = self.cursor.next

    def print_list(self):
        current = self.head.next
        while current != self.tail:
            print(current.value, end='')
            current = current.next
        print()

def solution():
    editor = LinkedList()
    initial_text = sys.stdin.readline().rstrip()
    for char in initial_text:
        editor.insert(char)

    n_iter = int(sys.stdin.readline().rstrip())
    commands = [sys.stdin.readline().rstrip() for _ in range(n_iter)]

    for command in commands:
        if command == "L":
            editor.move_left()
        elif command == "D":
            editor.move_right()
        elif command == "B":
            editor.delete()
        elif command.startswith("P"):
            _, char = command.split()
            editor.insert(char)

    editor.print_list()

if __name__ == "__main__":
    solution()