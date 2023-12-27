## https://www.acmicpc.net/problem/18870
import sys

N = int(input())
coords = list(sys.stdin.readline().rstrip().split())

sorted_coords = sorted(coords)
compress = {}
for item in sorted_coords:
    compress.update({item : sorted_coords.index(item)})

for item in coords:
    print(compress[item], end=" ")