def find_receivers(towers):
    stack = []
    receivers = [0] * len(towers)
    for i, height in enumerate(towers):
        while stack and stack[-1][1] < height:
            stack.pop()
        
        if stack:
            receivers[i] = stack[-1][0] + 1  # 인덱스는 0부터 시작하므로 +1
        
        stack.append((i, height))
        
    return receivers

N = int(input()) ## 5
towers = list(map(int, input().split())) ## [6 9 5 7 4]
receivers = find_receivers(towers)

print(' '.join(map(str, receivers)))