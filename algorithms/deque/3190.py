"""
https://www.acmicpc.net/problem/3190

어려운 점.
- 뱀이 어떻게 이동하는지 이해할 수가 없었다.
- 방향과 좌표에 대해 어떻게 컨트롤해야 할지 판단이 안됐다.


핵심사항.
- 벽이나 자신의 몸에 부딪히면 게임이 끝난다.
- 뱀의 이동 방향이 바뀐다.
- 뱀이 이동할 때 머리가 먼저 움직이고 해당 칸에 사과가 있으면 꼬리는 움직이지 않고, 칸에 사과거 없으면 꼬리가 따라온다. -> 머리와 꼬리가 같은 위치가 된다.

예제1에서 정답이 9인 이유는 while문이 마지막으로 play_time을 증가시키고 조건문에 의해 깨지기 때문이다.
"""

from collections import deque

## 보드 제작. 2차원 배열
N = int(input())

board = []
for _ in range(N):
    board.append([0] * N)

## 보드에 사과 추가.
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

## 방향 변환.
L = int(input())
dps = {}
for _ in range(L):
    second, direction = input().split()
    dps[int(second)] = direction

## 뱀의 좌표를 기록하기 위한 덱.
dq = deque()
dq.append((0, 0))

def change_direction(command, direction):
    if command == "L":
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

## 뱀의 이동을 위한 상하좌우를 의미하며 현재 좌표인 x, y에 값이 적용되어 현재 위치(행과 열)를 조정한다.
row_mover = [0, 1, 0, -1]
col_mover = [1, 0, -1, 0]

row, col = 0, 0
board[row][col] = 1
play_time = 0
direction = 0
## board에서 값이 1이면 뱀의 머리, 몸통, 꼬리 중 하나가 있음을 나타낸다.
## 따라서 else 문에서 현재 board의 칸에서 0 또는 2 이외의 값이 있으면 뱀의 일부에 부딪혔음을 의미한다.
while True:
    ## 게임시간 증가, 뱀의 이동.
    play_time += 1
    row += row_mover[direction]
    col += col_mover[direction]

    ## 벽에 부딪혔을 때 게임 종료
    if row < 0 or col < 0 or row >= N or col >= N:
        break

    if board[row][col] == 2:
        board[row][col] = 1
        dq.append((row, col))

        if play_time in dps:
            direction = change_direction(dps[play_time], direction)
    
    elif board[row][col] == 0:
        board[row][col] = 1
        dq.append((row, col))

        tail_row, tail_col = dq.popleft()
        board[tail_row][tail_col] = 0

        if play_time in dps:
            direction = change_direction(dps[play_time], direction)
    
    else: ## 뱀이 몸의 일부에 부딪혔을 때 게임 종료
        break

print(play_time)