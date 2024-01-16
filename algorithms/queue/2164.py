from collections import deque

N = int(input())
q = deque()

# 1부터 n까지의 카드를 큐에 넣는다.
for num in range(1, N + 1):
    q.append(num)

# 홀수번째에서는 맨 위 카드를 버리고, 짝수번째에서는 맨 위 카드를 맨 아래의 아래로 보낸다.
idx = 1
while len(q) > 1:
    if idx % 2 == 1:
        q.popleft()
    else:
        num = q.popleft()
        q.append(num)
    
    idx += 1

print(q[0])