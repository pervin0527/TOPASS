import sys

k = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))