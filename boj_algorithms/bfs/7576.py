"""
https://www.acmicpc.net/problem/7576
"""

from collections import deque

M, N = map(int, input().split())

box, days = [], []
all_ripe = True  # 모든 토마토가 익었는지 확인.
for _ in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    days.append([-1] * M)
    if 0 in row:
        all_ripe = False

# 모든 토마토가 이미 익었다면 0을 출력하고 프로그램 종료
if all_ripe:
    print(0)
    exit()

Q = deque()
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            Q.append((x, y))
            days[x][y] = 0
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while Q:
    x, y = Q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if box[nx][ny] == -1: ## 토마토가 들어 있지 않은 칸.
            continue

        if days[nx][ny] == -1 and box[nx][ny] == 0:
            days[nx][ny] = days[x][y] + 1
            Q.append((nx, ny))

# 모든 토마토가 익는 데 걸리는 시간을 찾는다.
max_days = max(map(max, days))

# 익지 않은 토마토가 있는지 확인.
for i in range(N):
    for j in range(M):
        if box[i][j] == 0 and days[i][j] == -1: ## 토마토가 익지 않았으면서, 익을 수 없는 환경인지 검사.
            max_days = -1
            break
    if max_days == -1:
        break


print(max_days)