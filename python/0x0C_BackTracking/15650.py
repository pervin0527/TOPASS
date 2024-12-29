def func(tmp):
    if tmp == m:
        str_res = " ".join([str(x) for x in result])
        print(str_res)
        return
    
    for i in range(n):
        if not is_used[i]:
            if tmp > 0 and result[tmp-1] > i + 1: ## 현재 선택된 숫자가 result[tmp-1]에 있는 숫자보다 큰가?
                continue
            result[tmp] = i + 1
            is_used[i] = True
            func(tmp+1)
            is_used[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    is_used = [False] * n

    func(0)