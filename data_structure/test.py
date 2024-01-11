## Linked List 구현.

class Node():
    """
    연결 리스트에 의해 연결될 노드에 대한 클래스를 정의한다.
    노드에 저장할 값은 (데이터, 다음 노드 주소, 이전 노드 주소)이다.
    self.next와 self.prev는 각각 다음 노드와 이전 노드의 주소를 저장하는 변수로 여기에 값이 저장되는 때는 노드 삽입이나 노드 삭제 단계이다.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self):
        """
        노드들을 활용한 연결리스트 클래스를 정의한다.
        head와 tail은 데이터 값을 저장하지 않는 더미 노드로, 노드 삽입이나 삭제 단계에서 예외 처리를 적용하지 않기 위해 사용한다.
        """
        self.head = None
        self.tail = None
        self.num_nodes = 0


    def search(self, n):
        """
        n번째 노드를 찾고, 그 노드가 가진 데이터 값을 반환한다.
        """
        i = 0
        curr_node = self.head.next
        while True:
            curr_node = curr_node.next

            if i == n:
                return curr_node
            

    def traverse(self):
        """
        연결리스트에 있는 모든 노드의 data를 출력한다.
        """
        if self.num_nodes > 0:
            curr_node = self.head.next # 첫번째 노드(시작 노드)

            for _ in range(0, self.num_nodes):
                print(curr_node.data)
                curr_node = curr_node.next
        else:
            print("연결 리스트에 노드가 존재하지 않습니다.\n")
        

    def insert(self, n, value):
        """
        n번째 노드의 다음에 새로운 노드를 삽입한다.
        1. 신규 노드의 next는 n번째 노드가 가리키던 n+1번째를 가리키고 n+1번째의 prev는 신규 노드를 가리킨다.
        2. n번째 노드의 next는 신규 노드를 가리키고, 신규 노드의 prev는 n번째 노드를 가리킨다.
        """
        new_node = Node(value)

        if self.num_nodes == 0:
            self.head.next = new_node
            new_node.prev = self.head

            self.tail.prev = new_node
            new_node.next = self.tail

        elif 0 < n < self.num_nodes:
            curr_node = self.search(n)

            new_node.next = curr_node.next      # 신규 노드의 next가 n+1번째 노드를 가리킨다.
            curr_node.next = new_node           # n번째 노드의 next가 신규 노드를 가리킨다.
            new_node.prev = curr_node           # 신규 노드의 prev가 n번째 노드를 가리킨다.
            curr_node.next.prev = new_node      # n+1번째 노드의 prev가 신규 노드를 가리킨다.

        self.num_nodes += 1


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.traverse()

    linked_list.insert(1, 10)
    linked_list.traverse()

    linked_list.insert(2, 20)
    linked_list.insert(3, 30)
    linked_list.traverse()