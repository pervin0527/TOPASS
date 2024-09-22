import sys
from typing import List
input = sys.stdin.readline

def dfs(graph, cx, cy, vis):
    area = 1
    vis[cx][cy] = True

    coord_x = [0, 0, -1, 1]
    coord_y = [-1, 1, 0, 0]
    for i in range(len(coord_x)):
        tx = cx + coord_x[i]
        ty = cy + coord_y[i]

        if tx < 0 or tx >= len(graph) or ty < 0 or ty >= len(graph[0]):
            continue

        if vis[tx][ty] or graph[tx][ty] == 0:
            continue

        area += dfs(graph, tx, ty, vis)

    return area

def solution():
    n, m = map(int, input().rstrip().split())

    paper = []
    for _ in range(n):
        line = list(map(int, input().rstrip().split()))
        paper.append(line)

    visited = [[False] * m for _ in range(n)]

    areas = []
    num_pics = 0
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1 and not visited[i][j]:
                num_pics += 1
                area = dfs(paper, i, j, visited)
                areas.append(area)

    print(num_pics)
    print(max(areas))

    
if __name__ == "__main__":
    solution()