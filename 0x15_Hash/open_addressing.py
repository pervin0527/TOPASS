class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        else:
            raise TypeError("Invalid key type. Only integers and strings are supported.")

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

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