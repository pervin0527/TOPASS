"""
https://www.acmicpc.net/problem/9012
"""
import sys

N = int(input())
# N = 1
for _ in range(N):
    stack = []
    line = sys.stdin.readline().rstrip()
    # line = "(()())((()))"

    for p in line:
        stack.append(p)
        
        if len(stack) > 1:
            if (stack[-1] == ")" and stack[-2] == "("):
                stack.pop()
                stack.pop()

    if len(stack) > 0:
        print("NO")
    else:
        print("YES")