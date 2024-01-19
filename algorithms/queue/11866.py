"""
https://www.acmicpc.net/problem/11866
"""

from collections import deque

q = deque()
result = []
N, K = map(int, input().split())

for number in range(1, N+1):
    q.append(number)

while len(q) > 1:
    for _ in range(K-1):
        q.append(q.popleft())
    
    target = q.popleft()
    result.append(target)

result.append(q.popleft())
result = str(result).replace("[", "<").replace("]", ">")
print(result)