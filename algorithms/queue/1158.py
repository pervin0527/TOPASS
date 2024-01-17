"""
https://www.acmicpc.net/problem/1158

10 8 -> <8, 6, 5, 7, 10, 3, 2, 9, 4, 1>
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

## 큐 사용
q = deque()
result = []

for i in range(1, N+1): 
    q.append(i)

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print(str(result).replace('[', '<').replace(']', '>'))

## 리스트 사용
# arr = [num for num in range(1, N+1)]
# idx = 0
# result = []

# for number in range(N):
#     idx += K - 1
#     if idx >= len(arr):
#         idx = idx % len(arr)
    
#     result.append(str(arr.pop(idx)))

# out = ", ".join(result)
# print(f"<{out}>")