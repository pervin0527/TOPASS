from collections import deque

dq = deque()
N, M = map(int, input().split())
target_indices = list(map(int, input().split()))

for i in range(1, N+1):
    dq.append(i)

cnt = 0
for target in target_indices:
    while True:
        if dq[0] == target:
            dq.popleft()
            break

        if dq.index(target) <= len(dq) // 2:
            item = dq.popleft()
            dq.append(item)
            cnt += 1

        else:
            item = dq.pop()
            dq.appendleft(item)
            cnt += 1

print(cnt)