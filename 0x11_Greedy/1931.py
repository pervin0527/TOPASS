import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().rstrip())
    arr = [[0, 0] for _ in range(N)]

    ## 끝나는 시간이 빠른 순으로, 같으면 시작 시간이 빠른 순으로 정렬
    for i in range(N):
        start_time, end_time = map(int, input().rstrip().split())
        arr[i][0], arr[i][1] = end_time, start_time

    arr.sort(key=lambda x : (x[0], x[1]))
    
    result = 0
    t = 0
    for i in range(N):
        ## 현재 회의가 끝나는 시간 보다 시작 시간이 빠른 회의는 건너뛴다.
        if t > arr[i][1]:
            continue
        
        result += 1
        t = arr[i][0]
    
    print(result)