from collections import deque

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    count = 0
    q = deque()
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and visited[x][y] == -1:
                q.append((x, y))
                visited[x][y] = 1
                count += 1

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            while q:
                tx, ty = q.popleft()
                for i in range(4):
                    cx = tx + dx[i]
                    cy = ty + dy[i]

                    if cx < 0 or cy < 0 or cx >= n or cy >= m:
                        continue
                    if graph[cx][cy] != 1 or visited[cx][cy] != -1:
                        continue
                    
                    q.append((cx, cy))
                    visited[cx][cy] = 1
    print(count)