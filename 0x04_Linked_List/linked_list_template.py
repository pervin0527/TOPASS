class Node:
    def __init__(self, data=None):
        self.data = data
        self.prv = None
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.nxt = self.tail
        self.tail.nxt = self.head
        self.num_nodes = 0
        
    def __repr__(self) -> str:
        cur_node = self.head.nxt

        result = ""
        while cur_node != self.tail:
            result += str(cur_node.data)
            cur_node = cur_node.nxt
            
            # if cur_node != self.tail:
            #     result += " -> "

        return result

    def insert(self, idx, data):
        if idx < 0 or idx > self.num_nodes:
            return False
        
        cur_node = self.head
        while idx > 0:
            cur_node = cur_node.nxt
            idx -= 1

        prev_node = cur_node
        next_node = cur_node.nxt

        new_node = Node(data)
        new_node.nxt = next_node
        new_node.prv = prev_node

        prev_node.nxt = new_node
        next_node.prv = new_node

        self.num_nodes += 1

        return True

    def delete(self, idx):
        if idx < 0 or idx > self.num_nodes:
            return False
        
        cur_node = self.head.nxt
        while idx > 0:
            cur_node = cur_node.nxt
            idx -= 1

        prev_node = cur_node.prv
        next_node = cur_node.nxt

        prev_node.nxt = next_node
        next_node.prv = prev_node
        
        self.num_nodes -= 1

        return True