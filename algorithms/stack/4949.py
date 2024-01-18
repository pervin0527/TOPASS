"""
https://www.acmicpc.net/problem/4949
"""

import sys

while True:
    stack = []
    sentence = sys.stdin.readline().rstrip()

    if sentence == ".":
        break

    for s in sentence:
        if s == "[" or s == "(":
            stack.append(s)

        elif s == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)

        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")