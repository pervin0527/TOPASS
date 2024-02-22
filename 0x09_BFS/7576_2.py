"""
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.

창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
"""

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())

all_ok = True
box, days = [], []
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    box.append(line)
    days.append([-1] * len(line))

    if 0 in line:
        all_ok = False

if all_ok:
    print(0)
    exit()

q = deque()
for x in range(n):
    for y in range(m):
        if box[x][y] == 1:
            q.append((x, y))
            days[x][y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    tx, ty = q.popleft()
    td = days[tx][ty]

    for idx in range(4):
        nx, ny = tx + dx[idx], ty + dy[idx]

        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        if box[nx][ny] == -1:
            continue

        if box[nx][ny] == 0 and days[nx][ny] == -1:
            q.append((nx, ny))
            days[nx][ny] = td + 1


max_days = max(map(max, days))
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and days[i][j] == -1:
            max_days = -1
            break
    if max_days == -1:
        break

print(max_days)