n = int(input())  # 체스판의 크기 N을 입력받음
cnt = 0  # 배치 가능한 경우의 수를 카운트하는 변수

# 사용 여부를 체크하는 배열들
isused1 = [False] * n  # 각 열에 퀸이 있는지 여부
isused2 = [False] * (2*n-1)  # / 방향 대각선에 퀸이 있는지 여부
isused3 = [False] * (2*n-1)  # \ 방향 대각선에 퀸이 있는지 여부

def func(cur):  # cur번째 행에 퀸을 배치하는 함수
    global cnt
    if cur == n:  # 모든 행에 퀸을 성공적으로 배치했다면
        cnt += 1
        return
    
    for i in range(n):  # i는 열을 의미
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:  # 해당 위치에 퀸을 놓을 수 없다면
            continue
        
        isused1[i] = True
        isused2[i + cur] = True
        isused3[cur - i + n - 1] = True
        func(cur + 1)  # 다음 행으로 넘어감

        ## 더 이상 넘어갈 수 없으면 이전 상태로 다시 되돌아옴
        isused1[i] = False
        isused2[i + cur] = False
        isused3[cur - i + n - 1] = False

func(0)  # 0번째 행부터 시작
print(cnt)  # 가능한 배치의 총 경우의 수를 출력
