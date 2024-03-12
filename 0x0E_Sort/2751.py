import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    numbers.sort()

    for n in numbers:
        print(n)