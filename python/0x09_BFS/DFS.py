## board 설정, 1은 파란 칸, 0은 빨간 칸
board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

N = len(board) ## 행의 갯수
M = len(board[0]) ## 열의 갯수

## 방문 여부를 기록할 리스트
visited = [[False] * M for _ in range(N)]

## 상하좌우 이동을 위한 델타 값
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

## BFS를 위한 큐
S = []

## 시작점 방문 처리 후 큐에 삽입
visited[0][0] = True
S.append((0, 0))

## BFS
while S:
    cur = S.pop()
    print(f'({cur[0]}, {cur[1]}) -> ', end='')

    for dir in range(4):  ## 상하좌우 검사
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]

        ## 좌표가 2차원 배열의 구조를 벗어나지 않았는지 검사.
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
            
        ## 방문 여부 및 칸의 색상 확인
        if visited[nx][ny] or board[nx][ny] != 1:
            continue

        ## 방문 처리 후 큐에 삽입
        visited[nx][ny] = True
        S.append((nx, ny))