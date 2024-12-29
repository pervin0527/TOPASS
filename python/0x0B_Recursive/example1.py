## 1부터 N까지의 수를 출력
def func(n):
    if n == 0:
        return
    
    print(n)
    func(n-1)

func(5)

## 피보나치 수열의 n번째 항
def func2(n):
    if n <= 1:
        return n

    return func2(n-1) + func2(n-2)