import sys

n = int(sys.stdin.readline().rstrip())
numbers = [x for x in range(1, n+1)]
sequence = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

stack = []
results = []
for target in sequence:
    while numbers and numbers[0] <= target:
        stack.append(numbers.pop(0))
        results.append("+")

    if stack[-1] == target:
        stack.pop()
        results.append("-")

    else:
        print("NO")
        break

else:
    for res in results:
        print(res)