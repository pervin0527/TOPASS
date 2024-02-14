n = int(input())
buildings = [int(input()) for _ in range(n)]

result = 0
stack = []
for building in buildings:
    while stack and building >= stack[-1]:
        stack.pop()
    stack.append(building)

    result += len(stack) - 1

print(result)