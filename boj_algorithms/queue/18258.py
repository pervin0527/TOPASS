"""
https://www.acmicpc.net/problem/18258

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

q = deque()
output = []

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])
    
    elif command[0] == "pop":
        output.append(str(q.popleft()) if q else '-1')

    elif command[0] == "size":
        output.append(str(len(q)))

    elif command[0] == "empty":
        output.append('0' if q else '1')
    
    elif command[0] == "front":
        output.append(str(q[0]) if q else '-1')

    elif command[0] == "back":
        output.append(str(q[-1]) if q else '-1')

print('\n'.join(output))
