import sys

n = int(sys.stdin.readline().rstrip())

commands = []
for _ in range(n):
    commands.append(sys.stdin.readline().rstrip().split())

result = []
stack = []
for command in commands:
    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack):
            result.append(stack.pop())
        else:
            result.append(-1)

    elif command[0] == "size":
        result.append(len(stack))

    elif command[0] == "empty":
        if len(stack):
            result.append(0)
        else:
            result.append(1)

    else:
        if len(stack):
            result.append(stack[-1])
        else:
            result.append(-1)

for res in result:
    print(res)