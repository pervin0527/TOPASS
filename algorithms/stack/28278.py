"""
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
"""
import sys

N = int(input()) ## 명령의 수

stack = []
commands = []
results = []
for _ in range(N):
    commands.append(sys.stdin.readline().rstrip().split())

for command in commands:
    if command[0] == "1":
        stack.append(command[1])

    elif command[0] == "2":
        if len(stack) > 0:
            # print(stack.pop())
            results.append(stack.pop())
        else:
            # print(-1)
            results.append(-1)

    elif command[0] == "3":
        # print(len(stack))
        results.append(len(stack))

    elif command[0] == "4":
        if len(stack) == 0:
            # print(1)
            results.append(1)
        else:
            # print(0)
            results.append(0)

    elif command[0] == "5":
        if len(stack) > 0:
            # print(stack[-1])
            results.append(stack[-1])
        else:
            # print(-1)
            results.append(-1)

for result in results:
    print(result)