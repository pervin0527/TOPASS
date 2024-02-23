from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001

q = deque()
q.append(n)
graph[n] = 0

dx = [-1, 1, 2]
while True:
    x = q.popleft()

    if x == k:
        print(graph[x])
        break

    for idx, i in enumerate(range(3)):
        if idx == 2:
            tx = x * dx[i]
        else:
            tx = x + dx[i]

        if tx < 0 or tx >= 100001:
            continue
        if graph[tx] != -1:
            continue
        
        q.append(tx)
        graph[tx] = graph[x] + 1