import sys
input = sys.stdin.readline

from collections import deque

def solution():
    T = int(input().rstrip())
    for t in range(T):
        P = input().rstrip()
        N = int(input().rstrip())
        arr = input().rstrip()

        arr = arr[1:-1].split(',')
        arr = deque(arr)

        if N == 0 and 'D' in P:
            print('error')
            continue

        is_error = False
        for p in P:
            if p == "R":
                arr.reverse()

            else:
                if len(arr) > 0:
                    arr.popleft()
                else:
                    is_error = True

        if is_error:
            print("error")
        else:
            arr = f"[{','.join(arr)}]"
            print(arr)

if __name__ == "__main__":
    solution()