import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
result = []

q = deque()
for num in range(1, N + 1):
    q.append(num)

pos = 0
while len(q) == 1:
    for i in range(1, K+1):
        if pos + i > len(q):
            pos = 0
        else:
            pos += i


# for idx, res in enumerate(result):
#     if idx == 0:
#         print(f"<{res},", end=" ")
#     elif idx == len(result) - 1:
#         print(f"{res}>", end=" ")
#     else:
#         print(f"{res},", end=" ")