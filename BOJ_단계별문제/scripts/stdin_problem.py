import sys

n_iter = int(sys.stdin.readline().rstrip())

for i in range(n_iter):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

## 5 1 1 12 34 5 500 40 60 1000 1000