def func(tmp):
    if tmp == 6:
        seq = ' '.join(str(x) for x in sorted(result))
        if seq not in checker:
            checker.add(seq)
            print(seq)
        return
    
    for i in range(k):
        if not used[i]:
            used[i] = True
            result[tmp] = s[i]
            func(tmp+1)
            used[i] = False


if __name__ == "__main__":
    inputs = []
    while True:
        line = list(map(int, input().split()))
        if line[0] == 0:
            break
        
        k = line[0]
        s = line[1:]
        inputs.append((k, s))

    for k, s in inputs:
        result = [0] * 6
        checker = set()
        used = [False] * k
        func(0)
        print()