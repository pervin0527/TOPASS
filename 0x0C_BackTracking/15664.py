def func(tmp, perm):
    if tmp == m:
        seq = " ".join([str(x) for x in perm])
        if seq not in checker:
            results.append(seq)
            checker.add(seq)
        return
    
    for i in range(n):
        if not used[i]:
            if perm and perm[tmp-1] > numbers[i]:
                continue
            perm.append(numbers[i])
            used[i] = True
            func(tmp+1, perm)
            used[i] = False
            perm.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    results = []
    checker = set()
    used = [False] * n
    func(0, [])

    for r in results:
        print(r)