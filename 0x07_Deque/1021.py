import sys
from collections import deque

def solution():
    N, M = map(int, input().split())
    targets = list(map(int, input().split()))

    dq = deque(range(1, N+1))

    cnt = 0
    for target in targets:
        idx = dq.index(target)
        if idx <= len(dq) // 2:
            # 왼쪽으로 회전
            for _ in range(idx):
                dq.append(dq.popleft())
                cnt += 1
        else:
            # 오른쪽으로 회전
            for _ in range(len(dq) - idx):
                dq.appendleft(dq.pop())
                cnt += 1
        dq.popleft()  # 첫 번째 원소 제거

    print(cnt)
            
if __name__ == "__main__":
    solution()