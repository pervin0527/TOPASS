"""
https://www.acmicpc.net/problem/2346
"""
from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
# 각 숫자의 인덱스를 저장
indexed_numbers = [(num, idx + 1) for idx, num in enumerate(numbers)]
dq = deque(indexed_numbers)

result = []

while dq:
    number, index = dq.popleft()
    result.append(index)

    if not dq:
        break

    if number > 0:
        dq.rotate(-(number - 1))
    else:
        dq.rotate(-number)

for r in result:
    print(r, end=" ")
