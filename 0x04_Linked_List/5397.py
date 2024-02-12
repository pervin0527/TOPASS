import sys

class Char:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data

class Editor:
    def __init__(self):
        self.head = Char()
        self.tail = Char()

        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail

    def insert(self, data):
        new_char = Char(data)
        new_char.next = self.cursor
        new_char.prev = self.cursor.prev

        self.cursor.prev.next = new_char
        self.cursor.prev = new_char

    def delete(self):
        if self.cursor.prev != self.head:
            self.cursor.prev.prev.next = self.cursor
            self.cursor.prev = self.cursor.prev.prev

    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def print_all(self):
        current = self.head.next
        while current != self.tail:
            print(current.data, end="")
            current = current.next
        print()

if __name__ == "__main__":
    n_iter = int(sys.stdin.readline().rstrip())
    for _ in range(n_iter):
        editor = Editor()
        sentence = sys.stdin.readline().rstrip()
        for s in sentence:
            if s == "<":
                editor.move_left()
            elif s == ">":
                editor.move_right()
            elif s == "-":
                editor.delete()
            else:
                editor.insert(s)
        editor.print_all()