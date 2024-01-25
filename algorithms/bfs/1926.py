"""
https://www.acmicpc.net/problem/1926

그래프를 아직 배우지 않았지만, BFS 강의에서 큐를 활용함.

6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

import sys
from collections import deque

N, M = map(int, input().split()) ## 도화지의 세로 크기, 가로 크기 -> row와 col 수

graph = []
check_list = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    check_list.append([False for _ in range(M)])

q = deque()
sizes = []
num_pictures = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
## x가 row_idx, y가 col_idx
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1 and check_list[x][y] == False:
            q.append((x, y))
            check_list[x][y] = True
            num_pictures += 1

        count = 0
        while q:
            tmp_x, tmp_y = q.popleft()
            count += 1
            for offset in range(0, 4):
                offset_x, offset_y = tmp_x + dx[offset], tmp_y + dy[offset]
                if 0 <= offset_x < N and 0 <= offset_y < M:
                    if graph[offset_x][offset_y] == 1 and check_list[offset_x][offset_y] == False:
                        q.append((offset_x, offset_y))
                        check_list[offset_x][offset_y] = True
        sizes.append(count)

print(num_pictures)
print(max(sizes) if sizes else 0)
