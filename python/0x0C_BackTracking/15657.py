def func(tmp):
    if tmp == m:
        print(" ".join(str(x) for x in result))
        return
    
    for i in range(n):
        if tmp > 0 and result[tmp-1] > numbers[i]:
            continue
        result[tmp] = numbers[i]
        func(tmp + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    result = [0] * m
    func(0)