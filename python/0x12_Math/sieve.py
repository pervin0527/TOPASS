def sieve(n):
    primes = [] ## 소수들을 저장할 리스트
    
    state = [True] * (n + 1) ## 에라토스테네스의 체
    state[1] = False ## 1은 소수가 아니니까 False

    for i in range(2, n+1):
        if not state[i]: ## i번째 칸이 False이면
            continue

        ## True이면 i를 제외한 모든 배수에 해당하는 칸을 False로 설정.
        for j in range(2 * i, n + 1, i): ## ex) i=2인 경우 4부터 N+1까지 4,6,8,...
            state[j] = False

    ## 모든 마킹 과정이 끝났으면 True인 원소들만 primes에 저장.
    for i in range(2, n + 1):
        if state[i]:
            primes.append(i)

    return primes