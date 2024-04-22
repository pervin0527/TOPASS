## 최대 공약수를 구하는 함수
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

## 최소 공배수를 구하는 함수
def lcm(a, b):
    return a // gcd(a, b) * b  ## a를 gcd(a, b)로 나누고 b를 곱한다.(IntOverflow 방지.)


def solve(m, n, x, y):
    ## x와 y가 각각 m과 n의 끝 값에 도달하면 0으로 처리.
    if x == m:
        x = 0
    if y == n:
        y = 0
    
    ## 최소 공배수가 마지막 해의 값.
    l = lcm(m, n)
    
    ## x에서 시작하여 m씩 증가하며 l까지 반복.
    for i in range(x, l + 1, m): ## 3, 13, 23, ...
        if i == 0:
            continue
        ## i가 n으로 나눈 나머지가 y라면 해당 값을 반환.
        if i % n == y:
            return i
    
    return -1

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        m, n, x, y = map(int, input().split())
        print(solve(m, n, x, y))
