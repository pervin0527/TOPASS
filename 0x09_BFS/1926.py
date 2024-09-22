import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, row, col, vis):
    q = deque()
    
    areas = []
    num_pics = 0
    x_coord = [0, 0, -1, 1]
    y_coord = [-1, 1, 0, 0]
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and vis[i][j] != True:
                q.append((i, j))
                num_pics += 1

            area = 0
            while q:
                cx, cy = q.popleft()
                vis[cx][cy] = True
                area += 1

                for k in range(len(x_coord)):
                    nx = cx + x_coord[k]
                    ny = cy + y_coord[k]

                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue

                    if vis[nx][ny] or graph[nx][ny] != 1:
                        continue

                    q.append((nx, ny))             
                    vis[nx][ny] = True
            
            areas.append(area)

    return num_pics, max(areas)


def solution():
    n, m = map(int, input().rstrip().split())

    paper = []
    for _ in range(n):
        line = list(map(int, input().rstrip().split()))
        paper.append(line)

    visited = [[False] * m for _ in range(n)]
    num_pics, max_area = bfs(paper, n, m, visited)
    print(num_pics)
    print(max_area)
    
if __name__ == "__main__":
    solution()