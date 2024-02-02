"""
https://www.acmicpc.net/problem/12789

사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다.
현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다.
"""
from collections import deque

N = int(input())
wait_line = deque(map(int, input().split())) ## 공간에서 다시 대기열로 들어오는게 불가능함.
stack = []

target = 1
while True:
    ## 대기열에 현재 순번의 사람이 있는가 확인.
    if wait_line and wait_line[0] == target:
        wait_line.popleft()
        target += 1
    else:
        stack.append(wait_line.popleft())

    ## 대기열에 존재하지 않으면, 빈 공간의 맨 위에 있는지 확인.
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

    ## 더 이상 대기하는 사람이 없는 경우 모두 간식을 받았음.
    if not wait_line and not stack:
        print("Nice")
        break

    ## 대기열에 사람이 없는데, 빈 공간에 사람의 순번이 맞지 않음 -> 필요한 순서대로 사람들을 줄세울 수 없는 상태
    elif not wait_line and stack[-1] != target:
        print("Sad")
        break