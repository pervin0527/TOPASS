## https://www.acmicpc.net/problem/1269
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

A = set(map(int, sys.stdin.readline().rstrip().split()))
B = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(A.difference(B)) + len(B.difference(A)))