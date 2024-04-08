import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    answer = 0
    for idx in range(len(coins)-1, -1, -1):
        coin = coins[idx]

        if K - coin >= 0:
            n_coin = K // coin
            answer += n_coin
            K -= (n_coin * coin)

    print(answer)