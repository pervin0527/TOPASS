def func(tmp):
    if tmp == m:
        print(" ".join(str(x) for x in result))
        return
    
    for i in range(n):
        if not is_used[i]:
            result[tmp] = numbers[i]
            is_used[i] = True
            func(tmp+1)
            is_used[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))

    result = [0] * m
    is_used = [False] * n
    func(0)