"""
https://pervin0527.notion.site/c7756a6cd9cf47e180ee076438638b1c?pvs=4

그리디 알고리즘에 대한 개념을 이해하고, 그에 대한 예제를 기록한다.

500원, 100원, 50원, 10원짜리 동전을 무수히 많이 가지고 있을 때, 거스름돈 N을 거슬러줄 수 있는 최소한의 동전 수를 구해라.
"""

n = 1260
count = 0
array = [500, 100, 50, 10]

for coin in array:
    ## 현재의 동전으로 거슬러 줄 수 있는 금액을 거스름 돈에서 차감하고, 동전의 수를 기록한다.
    count += n // coin
    n %= coin

print(count)