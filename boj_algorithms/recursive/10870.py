"""
https://www.acmicpc.net/problem/10870
"""
n = int(input())

def func(n):
    if n < 3:
        return 1
    return func(n-1) + func(n-2)

if n == 0:
    print(0)
else:
    print(func(n))