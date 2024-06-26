import sys
input = sys.stdin.readline

def solution1():
    n, k = map(int, input().rstrip().split())
    arr = [int(input().rstrip()) for _ in range(n)]
    
    counter = 0
    for a in arr[::-1]:
        while k // a > 0:
            k -= a
            counter += 1

    print(counter)

if __name__ == "__main__":
    solution1()