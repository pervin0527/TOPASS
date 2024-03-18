"""
입력에 대한 문제의 설명이 조금 어렵다.
"""

import sys

if __name__ == "__main__":
    inputs = sys.stdin.readlines()
    arr = []
    for inp in inputs:
        line = inp.rstrip().split()
        arr.extend(line)
    
    n = int(arr.pop(0))
    for i in range(n):
        arr[i] = int(arr[i][::-1])

    arr.sort()
    for item in arr:
        print(item)