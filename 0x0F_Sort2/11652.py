"""
-2^62부터 2^62의 범위이기 때문에 숫자 테이블을 만들어서 등장횟수를 카운트하는 방법이 불가능하다.
따라서 리스트를 정렬하고, 순회하면서 가장 많이 등장하는 원소를 갱신하는 방식을 수행한다.
"""

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(n)]

    nums.sort()
    count = 1
    max_count = 1
    max_value = nums[0]  ## 첫 번째 값으로 초기화

    for idx in range(1, n):  ## 첫 번째 요소는 이미 처리했으므로 1부터 시작
        if nums[idx] == nums[idx-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_value = nums[idx-1]
            count = 1  ## 새로운 숫자의 등장으로 카운트를 1로 재설정

    ## 마지막 숫자 카드에 대해서는 최대 등장 비교가 일어나지 못하기 때문에 사용.
    if count > max_count:
        max_value = nums[n-1]

    print(max_value)
