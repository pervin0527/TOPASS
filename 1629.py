"""
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

 - 지수 연산 법칙 a^n * a^n = a^2n
 - 모듈러 연산 A^B % C
    - B가 짝수이면 (A^(B/2) * A^(B/2)) % C
    - B가 홀수이면 (A^(B/2) * A^(B/2) * A) % C

"""

def solution(a, b, c):
    if b == 1:
        return a % c

    temp = solution(a, b // 2, c)

    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c

A, B, C = map(int, input().split())
print(solution(A, B, C))