"""
https://www.acmicpc.net/problem/1406
"""
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
        node.prev = self.cursor.prev
        node.next = self.cursor
        self.cursor.prev.next = node
        self.cursor.prev = node

    def delete(self):
        if self.cursor.prev != self.head:  # 삭제할 노드가 있으면
            self.cursor.prev.prev.next = self.cursor
            self.cursor.prev = self.cursor.prev.prev

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

editor = LinkedList()
initial_text = sys.stdin.readline().rstrip() # "dmih"
for char in initial_text:
    editor.insert(char)

n_iter = int(sys.stdin.readline().rstrip())
# commands = ["B", "B", "P x", "L", "B", "B", "B", "P y", "D", "D", "P z"]
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
