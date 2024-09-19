import sys
input = sys.stdin.readline
from collections import deque

def solution():
    T = int(input().rstrip())
    for t in range(T):
        P = input().rstrip()
        N = int(input().rstrip())
        arr = input().rstrip()

        if N == 0:
            arr = deque()  # N이 0일 경우 빈 deque
        else:
            arr = deque(arr[1:-1].split(','))  # 배열을 deque로 변환

        reversed_flag = False  # 뒤집어야 하는지 여부를 추적하는 플래그
        is_error = False

        for p in P:
            if p == "R":
                reversed_flag = not reversed_flag  # 뒤집을지 여부만 반전
            else:
                if arr:
                    if reversed_flag:
                        arr.pop()  # 뒤집힌 상태이면 뒤에서 제거
                    else:
                        arr.popleft()  # 정상 상태이면 앞에서 제거
                else:
                    is_error = True
                    break

        if is_error:
            print("error")
        else:
            if reversed_flag:
                arr.reverse()  # 마지막에 한 번만 뒤집기

            arr = f"[{','.join(arr)}]"
            print(arr)

if __name__ == "__main__":
    solution()
