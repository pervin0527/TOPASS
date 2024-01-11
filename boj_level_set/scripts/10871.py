import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = map(int, sys.stdin.readline().rstrip().split())

for item in A:
    if item < X:
        print(item)