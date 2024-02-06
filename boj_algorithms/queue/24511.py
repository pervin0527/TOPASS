"""
https://www.acmicpc.net/problem/24511
"""

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # 자료구조의 개수
A = list(map(int, sys.stdin.readline().rstrip().split())) # 자료구조. 0이면 큐, 1이면 스택
B = list(map(int, sys.stdin.readline().rstrip().split())) # i번째 자료구조에 들어있는 원소

M = int(sys.stdin.readline().rstrip()) # 삽입할 원소를 담고 있는 수열의 길이
C = list(map(int, sys.stdin.readline().rstrip().split())) # 수열

# 스택일 때는 의미가 없고, 큐일 때만 처리하면 된다.
# 다만, 큐들의 순서를 고려해 덱으로 처리
dq = deque()
for idx in range(N):
    if A[idx] == 0:
        dq.appendleft(B[idx])

for idx in range(M):
    dq.append(C[idx])
    print(dq.popleft(), end=" ")