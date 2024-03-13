def sort_func(x):
    n = len(x)
    for i in range(n): ## 각 반복마다 정렬해야 할 요소의 수가 하나씩 줄어든다.
        for j in range(n-i-1): ## n-i-1은 마지막 요소가 이미 정렬되었기 때문에, 불필요한 비교를 피하기 위함.
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    return x

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    print(sort_func(arr))