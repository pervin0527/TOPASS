def func(tmp, perm):
    if len(perm) == m:
        seq = " ".join([str(x) for x in perm])
        if seq not in checker:
            results.append(seq)
            checker.add(seq)
        return
    
    for i in range(n):
        if perm and perm[tmp-1] > numbers[i]:
            continue
        perm.append(numbers[i])
        func(tmp+1, perm)
        perm.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    results = []
    checker = set()
    func(0, [])

    for r in results:
        print(r)