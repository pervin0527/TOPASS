import sys
from collections import deque

def normal_bfs(g, n):
    count = 0
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    vis = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not vis[x][y]:
                q.append((x, y, g[x][y]))
                vis[x][y] = True
                count += 1

            while q:
                tx, ty, curr_color = q.popleft()
                for i in range(4):
                    cx = tx + dx[i]
                    cy = ty + dy[i]

                    if cx < 0 or cy < 0 or cx >= n or cy >= n:
                        continue
                    if g[cx][cy] != curr_color or vis[cx][cy] != False:
                        continue

                    vis[cx][cy] = True
                    q.append((cx, cy, g[cx][cy]))

    return count


def rg_bfs(g, n):
    count = 0
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    vis = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not vis[x][y]:
                q.append((x, y, g[x][y]))
                vis[x][y] = True
                count += 1

            while q:
                tx, ty, curr_color = q.popleft()
                for i in range(4):
                    cx = tx + dx[i]
                    cy = ty + dy[i]

                    if cx < 0 or cy < 0 or cx >= n or cy >= n:
                        continue
                    if vis[cx][cy] != False:
                        continue

                    if curr_color == g[cx][cy] or (curr_color in ['R', 'G'] and g[cx][cy] in ['R', 'G']):
                        vis[cx][cy] = True
                        q.append((cx, cy, g[cx][cy]))

    return count


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())

    graph = []
    visited = []
    for _ in range(n):
        graph.append([x for x in sys.stdin.readline().rstrip()])

    normal_result = normal_bfs(graph, n)
    rg_result = rg_bfs(graph, n)
    print(normal_result, rg_result)