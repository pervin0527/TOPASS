n = int(input())
towers = [(idx, tower) for idx, tower in enumerate(list(map(int, input().split())))]

stack = []
results = [0] * n
for idx, tower in towers:
    while stack and stack[-1][1] < tower:
        stack.pop()
    stack.append((idx, tower))

    if len(stack) > 1:
        results[idx] = stack[-2][0] + 1

results = " ".join([str(x) for x in results])
print(results)