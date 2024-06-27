import sys
input = sys.stdin.readline

def solution1():
    n, k = map(int, input().rstrip().split())
    arr = [int(input().rstrip()) for _ in range(n)]

    cnt = 0
    for i in range(n-1, -1, -1):
        m = k // arr[i]
        k -= (m * arr[i])
        cnt += m

    print(cnt)

if __name__ == "__main__":
    solution1()