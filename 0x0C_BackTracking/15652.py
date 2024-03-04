def func(tmp):
    if tmp == m:
        print(" ".join([str(x) for x in result]))
        return
    
    for i in range(n):
        if tmp > 0 and result[tmp-1] > i + 1:
            continue
        result[tmp] = i + 1
        func(tmp+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m

    func(0)