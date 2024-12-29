import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())
all_ok = True
q = deque()
boxes = []

visited = [[[False] * m for _ in range(n)] for _ in range(h)]
for _ in range(h):
    box = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        if 0 in row:
            all_ok = False
        box.append(row)
    boxes.append(box)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                q.append((i, j, k, 0)) # z, x, y, day
                visited[i][j][k] = True

if all_ok:
    print(0)
    exit()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
max_days = 0
while q:
    z, x, y, days = q.popleft()
    max_days = max(max_days, days)
    for i in range(len(dx)):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and not visited[nz][nx][ny] and boxes[nz][nx][ny] == 0:
            visited[nz][nx][ny] = True
            boxes[nz][nx][ny] = 1
            q.append((nz, nx, ny, days + 1))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                max_days = -1
                break
        if max_days == -1:
            break
    if max_days == -1:
        break

print(max_days)