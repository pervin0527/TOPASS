"""
https://www.acmicpc.net/problem/1919
"""

import sys
from string import ascii_lowercase

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

counter = {x : 0 for x in ascii_lowercase}
for s in str1:
    counter[s] += 1

for s in str2:
    counter[s] -= 1

result = 0
for c in counter.values():
    result += abs(c)

print(result)