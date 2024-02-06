"""
https://www.acmicpc.net/problem/27433
"""

def func(n):
    if n == 0:
        return 1
    return n * func(n-1)

N = int(input())
print(func(N))