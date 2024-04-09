"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().rstrip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

    arr.sort(key=lambda x : (x[0], x[1]))
    # print(arr)
    
    ## 첫번째 회의 선정.
    fs, fe = arr.pop(0)
    for i in range(1, N):
        if (fe - fs) > (arr[i][1] - arr[i][0]):
            fs, fe = arr.pop(i)
            break

    result = 1
    t = fe
    for i in range(N-2):
        if t > arr[i][0]:
            continue
        result += 1
        t = arr[i][1]

    print(result)
