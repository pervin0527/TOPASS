"""
https://www.acmicpc.net/problem/28279

1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
"""

import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "1":
        dq.appendleft(int(command[1]))
    
    elif command[0] == "2":
        dq.append(int(command[1]))

    elif command[0] == "3":
        if dq:
            print(dq.popleft())
        else:
            print("-1")
    
    elif command[0] == "4":
        if dq:
            print(dq.pop())
        else:
            print("-1")
    
    elif command[0] == "5":
        print(len(dq))

    elif command[0] == "6":
        print(0 if dq else 1)
    
    elif command[0] == "7":
        if dq:
            print(dq[0])
        else:
            print("-1")

    elif command[0] == "8":
        if dq:
            print(dq[-1])
        else:
            print("-1")