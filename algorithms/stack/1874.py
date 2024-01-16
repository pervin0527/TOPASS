"""
https://www.acmicpc.net/problem/1874
"""

N = int(input())

pos = 1
stack, result = [], []

for _ in range(N):
    n = int(input())

    while pos <= n:
        stack.append(pos)
        result.append("+")
        pos += 1

    if stack[-1] == n:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break

else:
    for r in result:
        print(r)