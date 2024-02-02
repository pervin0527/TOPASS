"""
https://www.acmicpc.net/problem/10845

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
from collections import deque

q = deque()
N = int(sys.stdin.readline().rstrip())

commands = []
for _ in range(N):
    commands.append(sys.stdin.readline().rstrip().split())

for command in commands:
    if command[0] == "push":
        q.append(command[1])
    
    elif command[0] == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif command[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])