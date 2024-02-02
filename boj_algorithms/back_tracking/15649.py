"""
https://www.acmicpc.net/problem/15649
"""

def func(k): ## 현재 k개까지의 수를 택한 상황에서 arr[k]를 정하는 함수.
    """
    맨 처음에는 아무런 수도 선택하지 않았으니 func(0)을 호출.
    func(0)은 arr[0]의 원소를 결정한 후에 func(1)을 호출.
    """

    ## Base condition. k가 m과 같으면 m개의 수를 모두 고른 상태이므로 종료.
    if k == m:
        for v in arr:
            print(v, end="")
        print()
        return
    
    ## 백트래킹의 핵심 부분. 
    ## 1부터 n까지의 수를 차례대로 확인하며 아직 사용되지 않은 수를 찾아낸다.
    for i in range(n):
        if isused[i] == False:
            arr[k] = i+1
            isused[i] = True
            func(k+1)
            isused[i] = False ## arr[k] = 0으로 하지 않는 이유는 어차피 다른 값으로 덮어쓰여지기 때문.


n, m = map(int, input().split())
arr, isused = [0] * m, [False] * n ## isused는 현재 상태에서 사용한 원소를 기록하기 위함.

func(0)