import sys
from typing import List
from collections import deque

input = sys.stdin.readline

def bfs(grh, dist):
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1

    x_coord = [-1, 1, 0, 0]
    y_coord = [0, 0, -1, 1]
    while q:
        cx, cy = q.popleft()
        cd = dist[cx][cy]

        for i in range(len(x_coord)):
            dx = cx + x_coord[i]
            dy = cy + y_coord[i]

            if dx < 0 or dx >= len(grh) or dy < 0 or dy >= len(grh[0]):
                continue

            if grh[dx][dy] != 1 or dist[dx][dy] != 0:
                continue

            q.append((dx, dy))
            dist[dx][dy] = cd + 1

    return dist

def solution():
    N, M = map(int, input().rstrip().split())
    
    graph = []
    distance = []
    for _ in range(N):
        line = input().rstrip()
        line = [int(x) for x in line]
        graph.append(line)

        distance.append([0 for _ in range(M)])

    distance = bfs(graph, distance)
    print(distance[N-1][M-1])

if __name__ == "__main__":
    solution()