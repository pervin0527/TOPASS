import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    numbers.sort(reverse=True)
    for n in numbers:
        print(n)