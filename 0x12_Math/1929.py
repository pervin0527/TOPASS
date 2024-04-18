if __name__ == "__main__":
    M, N = map(int, input().split())
    
    isprime_list = [True for _ in range(N+1)]
    isprime_list[0] = False ## 1은 소수에 해당하지 않으므로 False

    ## M부터 N까지의 수를 탐색
    # for i in range(2, N+1):
    for i in range(2, int(N**0.5)):
        ## is_prime의 i번째 원소가 False인 경우 건너뛴다.
        if not isprime_list[i]:
            continue

        # for j in range(i * 2, N+1, i):
        #     isprime_list[j] = False

        for j in range(i * i, N + 1, i):
            isprime_list[j] = False
        

    ## True로 남은 원소들만 반환.
    for i in range(M, N+1):
        if isprime_list[i]:
            print(i)