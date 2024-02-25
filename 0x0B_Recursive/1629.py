def func(a, b, c):
    if b == 1:
        return a % c
    
    tmp = func(a, b//2, c)

    if b % 2 == 0:
        return ((tmp ** (b//2)) * (tmp ** (b//2))) % c
    else:
        return (tmp * (tmp ** (b//2))) % c


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(func(a, b, c))