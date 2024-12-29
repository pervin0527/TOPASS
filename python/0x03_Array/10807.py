import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    v = int(input().strip())

    count = 0
    for number in arr:
        if number == v:
            count += 1

    print(count)

if __name__ == "__main__":
    solution()