def func(tmp):
    if tmp == m:
        print(" ".join([str(x) for x in result]))
        return

    for i in range(n):
        result[tmp] = numbers[i]
        func(tmp+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))

    result = [0] * m
    func(0)