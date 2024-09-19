import sys
from collections import deque

def solution():
    dq = deque()

    N = int(sys.stdin.readline().rstrip())
    commands = [sys.stdin.readline().rstrip() for _ in range(N)]

    for c in commands:
        c = c.split(" ")
        if c[0] == 'push_front':
            dq.appendleft(c[1])
        
        elif c[0] == 'push_back':
            dq.append(c[1])

        elif c[0] == 'pop_front':
            if dq:
                print(dq.popleft())
            else:
                print(-1)

        elif c[0] == 'pop_back':
            if dq:
                print(dq.pop())
            else:
                print(-1)   

        elif c[0] == 'size':
            print(len(dq))     

        elif c[0] == 'empty':
            if not dq:
                print(1)
            else:
                print(0)

        elif c[0] == 'front':
            if dq:
                print(dq[0])
            else:
                print(-1)

        elif c[0] == 'back':
            if dq:
                print(dq[-1])
            else:
                print(-1)
        
if __name__ == "__main__":
    solution()