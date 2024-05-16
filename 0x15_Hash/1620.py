import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().strip().split())
    
    name_to_number = {}
    number_to_name = [""] * (n + 1)
    
    for i in range(1, n + 1):
        name = input().strip()
        name_to_number[name] = i
        number_to_name[i] = name
    
    result = []
    for _ in range(m):
        query = input().strip()

        if query.isdigit():
            idx = int(query)
            result.append(number_to_name[idx])
        else:
            result.append(name_to_number[query])
    
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
