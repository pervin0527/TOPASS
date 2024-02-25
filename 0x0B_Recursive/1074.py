def func(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n-1) ## 2 ** 1 = 2
    if r < half and c < half: ## 4등분의 가로, 세로 중심선을 기준으로 몇사분면에 있는지 특정함.
        return func(n-1, r, c - half)
    
    if r < half and c >= half:
        return half * half + func(n-1, r, c-half)
    
    if r >= half and c < half:
        return 2 * half * half + func(n-1, r-half, c)
    
    return 3 * half * half + func(n-1, r-half, c-half)


if __name__ == "__main__":
    n, r, c = map(int, input().split()) ## 2, 3, 1
    print(func(n, r, c))