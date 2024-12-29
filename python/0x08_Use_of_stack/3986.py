import sys

n = int(sys.stdin.readline().rstrip())

count = 0
for _ in range(n):
    stack = []
    sentence = sys.stdin.readline().rstrip()

    for s in sentence:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    
    if not stack:
        count += 1

print(count)