import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = input().rstrip()

    stack = []
    for l in line:
        if l == "(":
            stack.append(l)
        elif l == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(l)

    if not stack:
        print("YES")
    else:
        print("NO")