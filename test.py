## https://www.acmicpc.net/problem/4948

def prime_checker(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


while True:
    cnt = 0
    N = int(input())
    if N == 0:
        break

    arr = [True] * (2 * N + 1)
    arr[0], arr[1] = False, False

    for i in range(2, int((2 * N) ** 0.5) + 1):
        if arr[i]:
            j = 2
            while i * j <= 2 * N:
                arr[i * j] = False
                j += 1

    print(arr[N+1:].count(True))

    # count= 0
    # for num in range(N+1, (2*N+1)):
    #     if prime_checker(num):
    #         count += 1
    #     else:
    #         continue
    
    # print(count)