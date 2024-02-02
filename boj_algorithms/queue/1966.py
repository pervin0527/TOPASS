"""
https://www.acmicpc.net/problem/1966

핵심 : M번째 문서의 위치를 계속해서 추적할 수 있는가
"""
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = [(pos, rank) for pos, rank in enumerate(map(int, input().split()))]
    arr = deque(arr)

    idx = 0
    while True:
        if arr[0][1] == max(arr, key=lambda x : x[1])[1]:
            idx += 1

            if arr[0][0] == M:
                print(idx)
                break

            else:
                arr.popleft()
        else:
            arr.append(arr.popleft())