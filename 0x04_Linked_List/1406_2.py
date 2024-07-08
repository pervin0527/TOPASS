import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """
    연결리스트 클래스.
    - 0번째 인덱스부터 시작.
    - head와 tail은 dummy node.
    """
    def __init__(self):
        self.num_nodes = 0

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self) -> str:
        results = ""
        curr_node = self.head.next
        for i in range(self.num_nodes):
            results += f"{curr_node.data}"
            curr_node = curr_node.next

            # if i < self.num_nodes - 1:
            #     results += " -> "

        return results

    def traverse(self):
        nodes = []
        curr_node = self.head.next
        for _ in range(self.num_nodes):
            nodes.append(curr_node.data)
            curr_node = curr_node.next

        return nodes

    def insert(self, idx, data):
        """
        연결리스트의 idx번째 위치에 새로운 노드를 삽입한다.
        - idx는 0부터 시작할 수 있으며 0보다 작거나 연결리스트가 가진 노드의 수보다 큰 인덱스를 입력하면 삽입을 수행하지 않는다.
        - head에서부터 시작하여 idx만큼 이동한 후 해당 위치에 신규 노드를 삽입한다.
        """
        if idx > self.num_nodes or idx < 0:
            return False

        new_node = Node(data)
        curr_node = self.head
        for _ in range(idx):
            curr_node = curr_node.next
        next_node = curr_node.next

        curr_node.next = new_node
        next_node.prev = new_node

        new_node.prev = curr_node
        new_node.next = next_node

        self.num_nodes += 1

        return True
    
    def delete(self, idx):
        """
        연결리스트의 idx번째 노드를 삭제한다.
        - insert와 다르게 0번째 노드부터 삭제할 노드가 있는 곳까지 이동.
        - head부터 시작하면 idx가 idx-1로 사용되는 것과 동일하기 때문에 제대로 된 삭제가 불가능함.
        """
        if idx > self.num_nodes or idx < 0:
            return False
        
        curr_node = self.head.next
        for _ in range(idx):
            curr_node = curr_node.next
        
        prev_node = curr_node.prev
        next_node = curr_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.num_nodes -= 1

        return True
    

def solution1():
    input_str = input().strip()
    num_commands = int(input())

    ll = LinkedList()
    for idx, ch in enumerate(input_str):
        ll.insert(idx, ch)

    cursor = len(input_str)-1
    for _ in range(num_commands):
        command = input().strip().split()
        if command[0] == 'L':
            if cursor > -1:
                cursor -= 1
        elif command[0] == 'D':
            if cursor < ll.num_nodes-1:
                cursor += 1
        elif command[0] == 'B':
            if cursor >= 0:
                ll.delete(cursor)
                cursor -= 1
        elif command[0] == 'P':
            cursor += 1
            ll.insert(cursor, command[1])

    print(ll)


if __name__ == "__main__":
    solution1()