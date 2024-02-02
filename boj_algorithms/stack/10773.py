"""
https://www.acmicpc.net/problem/10773
"""

stack = []
N = int(input())

for _ in range(N):
    n = int(input())

    if n == 0:
        stack.pop()

    else:
        stack.append(n)

print(sum(stack))