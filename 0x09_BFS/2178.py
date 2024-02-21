import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
check = []
for _ in range(n):
    line = [int(x) for x in sys.stdin.readline().rstrip()]
    graph.append(line)
    check.append([-1] * len(line))

q = deque()
q.append((0, 0))
check[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    tx, ty = q.popleft()
    td = check[tx][ty]

    for idx in range(4):
        cx, cy = tx + dx[idx], ty + dy[idx]

        if cx < 0 or cx >= n or cy < 0 or cy >= m:
            continue
        if graph[cx][cy] == 0 or check[cx][cy] > -1:
            continue

        q.append((cx, cy))
        check[cx][cy] = td + 1

print(check[-1][-1])