class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.num_nodes = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def __repr__(self):
        items = []
        curr_node = self.head
        for _ in range(self.num_nodes):
            curr_node = curr_node.next
            items.append(curr_node.value)
            
        return "LinkedList([" + ", ".join(map(str, items)) + "])"
    
    def search(self, idx):
        if idx < 0 or idx > self.num_nodes:
            return False
        
        curr_node = self.head.next
        for _ in range(idx):
            curr_node = curr_node.next

        return curr_node.value


    def insert(self, idx, value):
        if idx < 0 or idx > self.num_nodes:
            return False
        
        new_node = Node(value)

        curr_node = self.head
        for i in range(idx):
            curr_node = curr_node.next

        prev_node = curr_node
        next_node = curr_node.next

        new_node.next = next_node
        new_node.prev = prev_node
        prev_node.next = new_node
        next_node.prev = new_node
        self.num_nodes += 1


    def delete(self, idx):
        curr_node = self.head.next
        for _ in range(idx):
            curr_node = curr_node.next

        prev_node = curr_node.prev
        next_node = curr_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.num_nodes -= 1

        return curr_node.value
        


ll = LinkedList()
ll.insert(0, 10)
ll.insert(1, 15)
print(ll.search(0))
print(ll)

print(ll.delete(0))
print(ll)