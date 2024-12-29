import sys
input = sys.stdin.readline

def solution1():
    N, S = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))

    st = 0
    en = 0
    current_sum = 0
    min_len = sys.maxsize
    while en < N:
        current_sum += arr[en]
        en += 1

        while current_sum >= S:
            min_len = min(min_len, en - st)
            current_sum -= arr[st]
            st += 1

    if min_len == sys.maxsize:
        print(0)
    else:
        print(min_len)

if __name__ == "__main__":
    solution1()
