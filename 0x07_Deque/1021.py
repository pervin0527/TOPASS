import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
dq = deque([num for num in range(1, n+1)])
targets = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for target in targets:
    while True:
        if target == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(target) < len(dq) / 2:
                while dq[0] != target:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != target:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)