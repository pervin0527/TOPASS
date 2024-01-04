"""
https://www.acmicpc.net/problem/11399

N개의 소요 시간들이 주어졌을 때, 순서에 따른 시간 합이 달라진다.
따라서 각 단계마다 선택하는 시간을 최소 소요 시간으로 선택하고 이를 모두 더하면 총 합이 최소 시간이 될 것이다.

메모리 : 31120KB 소요 시간 : 48ms
"""

N = int(input())
times = list(map(int, input().split()))

arr = []
prev = 0
for _ in range(N):
    min_time = min(times)
    idx = times.index(min_time)
    prev += times.pop(idx)

    arr.append(prev)

print(sum(arr))