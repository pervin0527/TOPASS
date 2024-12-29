class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return
            prev = node
            node = node.next

# 예제 사용법
hash_table = HashTable(10)

# 정수 키-값 쌍 삽입
hash_table.insert(10, "Value 1")
hash_table.insert(20, "Value 2")
hash_table.insert(30, "Value 3")

# 문자열 키-값 쌍 삽입
hash_table.insert("apple", "Red fruit")
hash_table.insert("banana", "Yellow fruit")
hash_table.insert("orange", "Orange fruit")

# 값 검색
print(hash_table.search(10))  # "Value 1"
print(hash_table.search(20))  # "Value 2"
print(hash_table.search("apple"))  # "Red fruit"
print(hash_table.search("banana"))  # "Yellow fruit"

# 키-값 쌍 삭제
hash_table.delete(20)
hash_table.delete("apple")

# 삭제 후 검색
print(hash_table.search(20))  # None
print(hash_table.search("apple"))  # None