import sys

def solution():
    N = int(sys.stdin.readline().strip())

    commands = []
    for _ in range(N):
        command = sys.stdin.readline().strip()

        if " " in command:
            commands.append(command.split())
        else:
            commands.append(command)

    stack = []
    for command in commands:
        if isinstance(command, list) and command[0] == "push":
            stack.append(command[1])
        
        elif command == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        
        elif command == "size":
            print(len(stack))
        
        elif command == "empty":
            if stack:
                print(0)
            else:
                print(1)
        
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)
        

if __name__ == "__main__":
    solution()