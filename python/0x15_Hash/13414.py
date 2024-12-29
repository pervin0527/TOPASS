import sys
input = sys.stdin.readline

def hash_func(data, table_size):
    return (table_size + data % table_size) % table_size

def solution1():
    K, L = map(int, input().split())
    arr = [input().strip() for _ in range(L)]
    
    table_size = 1000003
    table = [0] * table_size
    
    seen = set()
    check_list = []
    for i in range(L):
        data = arr[i]
        hash_value = hash_func(int(data), table_size)
        table[hash_value] = data

        # 중복된 학번 처리
        if data in seen:
            check_list.remove(data)
        
        check_list.append(data)
        seen.add(data)

    for i in range(K):
        print(check_list[i])
    
if __name__ == "__main__":
    solution1()