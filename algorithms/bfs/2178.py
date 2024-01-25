"""
https://www.acmicpc.net/problem/2178

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111111
"""
import sys
from collections import deque

N, M = map(int, input().split())

maze = []
dist = []

for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
    dist.append([-1] * M)

q = deque()
q.append((0, 0, 1))  # 시작점과 시작점의 거리를 1로 설정
dist[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    row_idx, col_idx, cur_dist = q.popleft()

    for idx in range(4):
        tmp_row = row_idx + dx[idx]
        tmp_col = col_idx + dy[idx]

        if 0 <= tmp_row < N and 0 <= tmp_col < M:
            if maze[tmp_row][tmp_col] == "1" and dist[tmp_row][tmp_col] == -1:
                q.append((tmp_row, tmp_col, cur_dist + 1))
                dist[tmp_row][tmp_col] = cur_dist + 1

print(dist[N-1][M-1])
