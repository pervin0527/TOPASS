"""
https://www.acmicpc.net/problem/2577
"""

a = int(input())
b = int(input())
c = int(input())

res = a * b * c
counter = {}
for num in range(0, 10):
    counter[str(num)] = 0

for r in str(res):
    counter[r] += 1

for v in list(counter.values()):
    print(v)