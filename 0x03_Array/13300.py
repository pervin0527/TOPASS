"""
https://www.acmicpc.net/problem/13300
"""
import sys
import math

N, K = map(int, sys.stdin.readline().rstrip().split())

cnt_dict = {}
for _ in range(N):
    gender, grade = map(int, sys.stdin.readline().rstrip().split())
    if f"{grade}_{gender}" not in cnt_dict:
        cnt_dict[f"{grade}_{gender}"] = 1
    else:
        cnt_dict[f"{grade}_{gender}"] += 1

# print(cnt_dict)

count = 0
for v in list(cnt_dict.values()):
    if v == 0:
        continue
    
    count += math.ceil(v / K)

print(count)