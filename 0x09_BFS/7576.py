import sys
from typing import List
from collections import deque

input = sys.stdin.readline

def bfs(graph: List, distance: List, q: deque):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        d = distance[x][y]

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx >= len(graph) or ty < 0 or ty >= len(graph[0]):
                continue

            if distance[tx][ty] > -1  or graph[tx][ty] != 0:
                continue

            q.append((tx, ty))
            distance[tx][ty] = d + 1

    return distance

def solution():
    M, N = map(int, input().rstrip().split())

    graph = []
    distance = []
    
    q = deque()
    all_ok1 = True
    for i in range(N):
        row = list(map(int, input().rstrip().split()))
        distance.append([-2] * M)
        for j in range(M):
            if row[j] == 1:
                q.append((i, j))
                distance[i][j] = 0
            elif row[j] == 0: 
                all_ok1 = False
                distance[i][j] = -1

        graph.append(row)

    if all_ok1:
        print(0)
    else:
        distance = bfs(graph, distance, q)
        # max_value = max(max(row) for row in distance)
        # print(max_value)

        max_value = 0
        all_ok2 = True
        for row in distance:
            for elem in row:
                if elem == -1:
                    all_ok2 = False
                elif max_value < elem:
                    max_value = elem

        if all_ok2:
            print(max_value)
        else:
            print(-1)


if __name__ == "__main__":
    solution()