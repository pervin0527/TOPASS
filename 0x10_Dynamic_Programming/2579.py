if __name__ == "__main__":
    n = int(input())
    s = [0] * 305  # 계단 점수를 저장할 리스트
    d = [[0, 0, 0] for _ in range(305)]  # DP 테이블

    # 계단 점수 입력 받기, 인덱스를 1부터 시작하도록 조정
    for i in range(1, n+1):
        s[i] = int(input())

    # n이 1일 경우, 첫 번째 계단의 점수 출력 후 종료
    if n == 1:
        print(s[1])
        exit()

    # 초기 조건 설정
    d[1][1] = s[1]
    d[1][2] = 0
    d[2][1] = s[2]
    d[2][2] = s[1] + s[2]

    # DP를 사용하여 i번째 계단까지의 최대 점수 계산
    for i in range(3, n+1):
        d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
        d[i][2] = d[i-1][1] + s[i]

    # n번째 계단까지의 최대 점수 출력
    print(max(d[n][1], d[n][2]))
