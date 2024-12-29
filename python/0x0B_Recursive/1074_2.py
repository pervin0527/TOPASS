def func(n, row, col):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    if row < half and col < half:
        return func(n-1, row, col)
    elif row < half and col >= half:
        return half * half + func(n-1, row, col-half)
    elif row >= half and col < half:
        return 2 * half * half + func(n-1, row-half, col)
    else:
        return 3 * half * half + func(n-1, row-half, col-half)
    
n, r, c = map(int, input().split())
print(func(n, r, c))