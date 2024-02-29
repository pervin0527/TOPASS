def func(k):
    if k == m: ## 더 이상 선택할 수 있는 옵션이 없을 때.
        print(" ".join([str(x) for x in results]))
        return
    
    for i in range(n):
        if not options[i]:
            options[i] = True
            results[k] = i + 1
            func(k+1)
            options[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split()) ## 4, 3

    results = [0] * m
    options = [False] * n
    func(0)