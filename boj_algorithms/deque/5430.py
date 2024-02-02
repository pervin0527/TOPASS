"""
https://www.acmicpc.net/problem/5430

핵심 처리
R
0
[]
"""

from collections import deque

T = int(input())
for _ in range(T):
    funcs = [x for x in input()]
    n = int(input())

    if n > 0:
        arr = deque([int(x) for x in input()[1:-1].split(',')])
    else:
        _ = input()
        arr = deque()
    
    reverse = False
    for f in funcs:
        if f == "R":
            reverse = False if reverse else True
        else:
            if len(arr) == 0:
                print("error")
                break

            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
    else:
        arr = list(arr)
        if reverse:
            arr = arr[::-1]
        result = ",".join(str(item) for item in arr)
        print("[" + result + "]")
