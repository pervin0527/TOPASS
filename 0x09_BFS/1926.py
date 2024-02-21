import sys
from collections import deque

N, M = map(int, input().split())

board, check = [], []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    check.append([False for _ in range(M)])


Q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

areas = []
num_pictures = 0
for x in range(N):
    for y in range(M):
        if board[x][y] == 1 and check[x][y] == False:
            Q.append((x, y))
            check[x][y] = True
            num_pictures += 1
            area = 0

        while Q:
            tx, ty = Q.popleft()
            area += 1

            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if board[nx][ny] == 0 or check[nx][ny] == True:
                    continue

                Q.append((nx, ny))
                check[nx][ny] = True

            areas.append(area)

print(num_pictures)
print(max(areas) if areas else 0)