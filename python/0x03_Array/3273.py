"""
https://www.acmicpc.net/problem/3273

a1부터 an까지 n개의 서로 다른 양의 정수로 구성된 수열이 있을 때
자연수 x가 주어지면 ai+aj=x를 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성해라.
i < j임에 주의할 것.
"""

import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

numbers.sort()  # 수열 정렬
left, right = 0, n - 1  # 투 포인터로 양끝에서부터 가운데로 모여들며 탐색한다.
count = 0

while left < right:
    current_sum = numbers[left] + numbers[right]
    
    if current_sum == x:
        count += 1
        left += 1
        right -= 1
    elif current_sum < x: ## x보다 합이 작으면 값을 키워야하므로, 왼쪽 포인터를 오른쪽으로 한 칸 이동시킨다.
        left += 1
    else: ## x보다 합이 크다면, 값을 줄여아하므로 오른쪽 포인터를 왼쪽으로 한 칸 이동시킨다.
        right -= 1

print(count)