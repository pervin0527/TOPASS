from collections import deque

# 입력 받기
R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

# 불과 지훈이의 위치 찾기
fire_queue = deque()
jihun_queue = deque()
fire_time = [[-1] * C for _ in range(R)]  # 불이 도착하는 시간
jihun_time = [[-1] * C for _ in range(R)] # 지훈이가 도착하는 시간

# 불과 지훈이의 시작 위치 저장
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fire_queue.append((i, j))
            fire_time[i][j] = 0  # 불의 시작점은 시간 0
        elif maze[i][j] == 'J':
            jihun_queue.append((i, j))
            jihun_time[i][j] = 0  # 지훈이의 시작점은 시간 0

## fire_time과 jihun_time은 -1과 0으로만 구성된 상태.

# 4방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 불 BFS
while fire_queue:
    x, y = fire_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and fire_time[nx][ny] == -1 and maze[nx][ny] != '#': ## fire_time[nx][ny]가 -1이면서 maze[nx][ny]가 #이 아니면 이동할 수 있는 경로..
            fire_time[nx][ny] = fire_time[x][y] + 1
            fire_queue.append((nx, ny))

# 지훈이 BFS
while jihun_queue:
    x, y = jihun_queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 미로 탈출 조건: 가장자리에서 탈출
        if nx < 0 or nx >= R or ny < 0 or ny >= C: ## nx, ny에 대해 0보다 작거나(음수) R, C보다 큰 경우 배열의 범위를 벗어나는 좌표가 되므로 탈출에 성공했음을 뜻함.
            print(jihun_time[x][y] + 1)
            exit()

        # 지훈이가 이동할 수 있는 경우: 벽이 아니고, 방문한 적이 없으며, 불이 도착하기 전에 이동
        ## maze[nx][ny] != '#' 벽이 아니면서 jihun_time[nx][ny] == -1이면 이동이 가능한 것. 
        if 0 <= nx < R and 0 <= ny < C and jihun_time[nx][ny] == -1 and maze[nx][ny] != '#':
            if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                jihun_time[nx][ny] = jihun_time[x][y] + 1
                jihun_queue.append((nx, ny))

# 탈출 불가능한 경우
print("IMPOSSIBLE")
