class Node:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.item = value

class LinkedList:
    def __init__(self):
        self.n_nodes = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def search(self, n):
        if n < 0 or n > self.n_nodes + 1:
            return
        
        idx = 1
        current_node = self.head.next
        while current_node != self.tail:
            if idx == n:
                return current_node
            current_node = current_node.next
            idx += 1
        
        return

    def insert(self, n, v):
        new_node = Node(v)

        if n == 1:
            new_node.next = self.head.next
            new_node.prev = self.head

            self.head.next.prev = new_node
            self.head.next = new_node
        else:
            prev_node = self.search(n-1)
            if prev_node is None:
                return
            new_node.next = prev_node.next
            new_node.prev = prev_node

            prev_node.next.prev = new_node
            prev_node.next = new_node

        self.n_nodes += 1

    def remove(self, n):
        current_node = self.search(n)
        if current_node is None:
            return

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        self.n_nodes -= 1

    def traverse(self):
        items = []
        current_node = self.head.next
        while current_node != self.tail:
            items.append(current_node.item)
            current_node = current_node.next

        return items
    
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert(1, 10)
    print(ll.traverse())

    ll.insert(2, 20)
    print(ll.traverse())

    ll.insert(3, 30)
    print(ll.traverse())

    ll.remove(2)
    print(ll.traverse())

    ll.remove(1)
    ll.remove(1)
    ll.remove(1)
    print(ll.traverse())