import sys

line = sys.stdin.readline().rstrip()

count = 0
stack = []
razer = False
for l in line:
    if l == "(":
        if stack:
            stack[-1] = (False, "(")
        stack.append((True, "("))

    elif l == ")":
        if stack[-1][0]:
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)