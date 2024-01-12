class Node:
    """
    연결 리스트에 의해 연결될 노드에 대한 클래스를 정의한다.
    노드에 저장할 값은 (데이터, 다음 노드 주소, 이전 노드 주소)이다.
    self.next와 self.prev는 각각 다음 노드와 이전 노드의 주소를 저장하는 변수로 여기에 값이 저장되는 때는 노드 삽입이나 노드 삭제 단계이다.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        """
        노드들을 활용한 연결리스트 클래스를 정의한다.
        head와 tail은 데이터 값을 저장하지 않는 더미 노드로, 노드 삽입이나 삭제 단계에서 예외 처리를 적용하지 않기 위해 사용한다.
        """
        self.num_nodes = 0

        self.head, self.tail = Node(None), Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def search(self, n):
        """
        연결 리스트에서 n번째 노드를 찾는 메서드.
        1부터 시작하는 인덱스를 사용하며, 존재하지 않는 인덱스에 대해서는 None을 반환한다.
        """
        current = self.head.next
        index = 1
        while current != self.tail:
            if index == n:
                return current
            current = current.next
            index += 1
        return None

    def insert(self, n, data):
        """
        연결 리스트의 n번째 위치에 새로운 노드를 삽입하는 메서드.
        1부터 시작하는 인덱스를 사용하며, 존재하지 않는 인덱스에 대해서는 삽입을 수행하지 않는다.
        """
        new_node = Node(data)

        if n == 1:  # 리스트의 처음에 삽입하는 경우
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node
        else:
            prev_node = self.search(n - 1)
            if prev_node is None or prev_node == self.tail:
                return  # 존재하지 않는 위치에는 삽입하지 않음

            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node

        self.num_nodes += 1

    def traverse(self):
        """
        연결 리스트의 모든 노드를 순회하며 데이터를 출력하는 메서드.
        """
        current = self.head.next
        while current != self.tail:
            print(current.data)
            current = current.next

# 예시: LinkedList 클래스의 메서드를 사용하여 몇 가지 작업을 수행
ll = LinkedList()
ll.insert(1, 10)
ll.insert(2, 20)
ll.insert(2, 15)
ll.insert(3, 30)
ll.traverse()