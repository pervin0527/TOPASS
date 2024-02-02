"""
https://www.acmicpc.net/problem/9663
"""

## func(0)을 호출해 0번째 행에 퀸을 배치한다.
## func(0)은 func(1)을 호출해 1번째 행에 퀸을 배치한다.
## func(n)까지 도달했다면, 모든 행에 퀸을 배치할 수 있으므로 count + 1
## 특정 좌표에 퀸을 어떻게 둘 것인가?

def func(cur):
    global count
    if cur == n:
        count += 1
        return
    
    for i in range(n):
        if isused1[i] or isused2[i+cur] or isused3[cur-i+n-1]:
            continue
        isused1[i] = True
        isused2[i+cur] = True
        isused3[cur-i+n-1] = True
        func(cur+1)
        isused1[i] = False
        isused2[i+cur] = False
        isused3[cur-i+n-1] = False


n = int(input())

count = 0
isused1 = [False] * n ## column에 대응되는 값. (x, y)에 퀸이 있으면 isused1[y]=True
isused2 = [False] * (2*n) ## 좌측 하단과 우측 상단을 연결하는 대각선. (x, y)에 퀸이 있으면 isused2[x+y]=True
isused3 = [False] * (2*n) ## 좌측 상단과 우측 하단을 연결하는 대각선. (x, y)에 퀸이 있으면 isused3[x-y+n-1]=True

func(0)
print(count)