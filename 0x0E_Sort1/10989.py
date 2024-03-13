import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = [0] * 10001

    for _ in range(n):
        v = int(sys.stdin.readline())
        numbers[v] += 1

    for i in range(len(numbers)):
        for _ in range(numbers[i]):
            print(i)