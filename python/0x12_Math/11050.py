def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i

    return f

if __name__ == '__main__':
    n, k = map(int, input().split())

    t1 = factorial(n-k)
    t2 = factorial(k)
    t = t1 * t2

    h = factorial(n)

    print(int(h/t))