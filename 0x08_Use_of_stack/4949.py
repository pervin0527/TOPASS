import sys

while True:
    stack = []
    sentence = sys.stdin.readline().rstrip()

    if sentence == ".":
        break

    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
        else:
            continue

    if not stack:
        print("yes")
    else:
        print("no")
