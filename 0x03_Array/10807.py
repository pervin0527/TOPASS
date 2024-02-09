"""
https://www.acmicpc.net/problem/10807

총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구해라.
"""
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

checker = [0] * 202
for d in arr:
    checker[d] += 1

print(checker[v])