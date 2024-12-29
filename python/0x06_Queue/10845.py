import sys
from collections import deque

def solution():
    queue = deque()
    
    N = int(sys.stdin.readline())
    commands = [sys.stdin.readline().rstrip() for _ in range(N)]
    
    for command in commands:
        command = command.split(' ')

        if command[0] == "push":
            queue.append(command[1])
        
        elif command[0] == 'pop':
            if queue:
                v = queue.popleft()
                print(v)
            else:
                print(-1)
        
        elif command[0] == 'size':
            print(len(queue))

        elif command[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)
        
        elif command[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        
        elif command[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)

if __name__ == "__main__":
    solution()