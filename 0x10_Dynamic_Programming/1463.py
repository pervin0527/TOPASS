if __name__ == "__main__":
    n = int(input())

    ## 1.테이블 정의
    table = [0] * (n + 1) ## 0번째 원소는 0번째 항을 의미하기 때문에 사용하지 않으므로 n+1

    ## 2.점화식 찾기. & 3.초기값 찾기.
    ## i = 1일 때 이미 1이므로 D[1] = 0
    ## i = 2일 때 i-1=1, i//2=1 이므로 1
    for i in range(2, n+1):
        """
        +1을 하는 이유는 연산 횟수 카운팅을 위함. 예를 들어 i=4 일 경우
         - table[4-1]은 table[3]이다. 
         - table[3]은 3으로 나누어 떨어지는 한 번의 연산이 필요하므로, table[3]=1이다.
         - table[4]는 여기서 1을 빼는 한 번의 연산이 더 필요하므로 table[i-1]+1 이 된다.
        """
        table[i] = table[i-1] + 1

        if i % 2 == 0:
            table[i] = min(table[i], table[i//2]+1)

        if i % 3 == 0:
            table[i] = min(table[i], table[i//3]+1)

    print(table[n])
