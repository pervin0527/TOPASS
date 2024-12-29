def func(start, end, n): ## 1, 3, 3
    if n == 1:
        print(start, end)
        return
    
    func(start, 6-start-end, n-1) ## 1, 6-1-3=2, 2 ---> 1, 6-1-2=3, 1
    print(start, end) ## 1, 2, 2
    func(6-start-end, end, n-1)


if __name__ == "__main__":
    n = int(input())
    
    print(2 ** n - 1)
    func(1, 3, n)