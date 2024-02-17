"""
우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
"""

from collections import deque

n = int(input())
q = deque([x for x in range(1, n+1)])

while q:
    if len(q) == 1:
        break

    first = q.popleft()
    q.append(q.popleft())

print(q[0])