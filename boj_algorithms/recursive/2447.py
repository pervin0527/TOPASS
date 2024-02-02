"""
https://www.acmicpc.net/problem/2447
"""

n = int(input())
result = [[" " for _ in range(n)] for _ in range(n)]

def func(n, x, y):
    if n == 1:
        result[y][x] = "*"
        return

    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            func(div, x+j*div, y+i*div)

func(n, 0, 0)
for row in result:
    print(''.join(row))