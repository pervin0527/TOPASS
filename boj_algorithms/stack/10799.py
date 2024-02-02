"""
https://www.acmicpc.net/problem/10799

핵심
    1. 현재 문자가 )이고, top 원소가 (일 때 레이저인가 막대의 우측 끝인가 구분.
    2. 현재 문자가 )일 때, 우측 막대의 끝일 경우에 대한 처리.
"""

import sys

total = 0
stack = []
line = sys.stdin.readline().rstrip()

for l in line:        
    if l == "(":
        if len(stack) > 0:
            stack[-1][1] = False
        stack.append(["(", True])

    else:
        _, is_raiser = stack[-1]
        if is_raiser:
            stack.pop()
            total += len(stack)
        else:
            total += 1
            stack.pop()

print(total)