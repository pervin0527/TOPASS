"""
https://www.acmicpc.net/problem/7576
"""

from collections import deque

M, N = map(int, input().split())

box, days = [], []
for _ in range(N):
    box.append(list(map(int, input().split())))
    days.append([-1 for _ in range(M)])

zero_count = 0
Q = deque()
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            Q.append((x, y))
            days[x][y] = 0
        
        elif box[x][y] == 0:
            zero_count += 1

if zero_count == 0:
    print(0)

else:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if box[nx][ny] == -1 or box[nx][ny] == 1:
                continue

            if days[nx][ny] == -1:
                days[nx][ny] = days[x][y] + 1
                Q.append((nx, ny))

max_days = max(map(max, days))

# 익지 않은 토마토가 있는지 확인.
for x in range(N):
    for y in range(M):
        if box[x][y] == 0 and days[x][y] == -1:
            max_days = -1  # 익지 않은 토마토가 있으므로 -1을 할당.
            break
    if max_days == -1:
        break

print(max_days)
