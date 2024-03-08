def sort_func(x):
    n = len(x)
    for i in range(n):
        tmp = i ## 현재 단계에서 맨 앞 자리.
        for j in range(i+1, n):
            if x[tmp] > x[j]:
                tmp = j
        x[i], x[tmp] = x[tmp], x[i]

    return x

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    print(sort_func(arr))