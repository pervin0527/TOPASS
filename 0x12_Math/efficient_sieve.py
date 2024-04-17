def sieve_efficient(n):
    primes = []

    state = [True] * (n + 1)
    state[1] = False

    for i in range(2, int(n**0.5) + 1): ## 2부터 n의 제곱근까지만 순회.
        if not state[i]:
            continue

        """
        i * 2가 아니라 i * i로 각 수의 제곱부터 시작.
        i=2일 때 4,6,8,10,12,...
        i=3일 때 9,12,15,...
        i=5일 때 25,30,...

        중복되는 숫자들을 조금이라도 줄여 알고리즘의 효율성을 높인다.
        """
        for j in range(i * i, n + 1, i):
            state[j] = False

    for i in range(2, n + 1):
        if state[i]:
            primes.append(i)
    return primes
