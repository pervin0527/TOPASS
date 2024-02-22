from collections import deque

def bfs_fire_spread(maze, fire_spread, R, C):
    q = deque()
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':  # 불이 시작하는 위치
                q.append((i, j))
                fire_spread[i][j] = 0  # 불이 시작하는 위치의 확산 시간은 0
    
    # 불의 확산 계산
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] != '#' and fire_spread[nx][ny] == -1:
                    fire_spread[nx][ny] = fire_spread[x][y] + 1
                    q.append((nx, ny))

def bfs_escape(maze, fire_spread, R, C, start):
    q = deque([(*start, 0)])  # 지훈이의 위치와 시작 시간
    visited = [[False]*C for _ in range(R)]
    visited[start[0]][start[1]] = True
    
    while q:
        x, y, time = q.popleft()
        if x == 0 or x == R-1 or y == 0 or y == C-1:  # 탈출 조건
            return time + 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' and not visited[nx][ny]:
                    if fire_spread[nx][ny] == -1 or fire_spread[nx][ny] > time + 1:
                        visited[nx][ny] = True
                        q.append((nx, ny, time + 1))
    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]
fire_spread = [[-1]*C for _ in range(R)]  # 불의 확산 시간을 저장할 배열

# 불의 확산 시간 계산
bfs_fire_spread(maze, fire_spread, R, C)

# 지훈이의 초기 위치 찾기
start = None
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            start = (i, j)
            break
    if start:
        break

# 지훈이의 탈출 경로 계산
result = bfs_escape(maze, fire_spread, R, C, start)
print(result)
