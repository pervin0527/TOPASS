import sys

line = sys.stdin.readline().rstrip()

stack = []
tmp, result = 1, 0
for i in range(len(line)):
    if line[i] == "(":
        stack.append(line[i])
        tmp *= 2
    elif line[i] == "[":
        stack.append(line[i])
        tmp *= 3
    elif line[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        elif line[i-1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        elif line[i-1] == "[":
            result += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(result)