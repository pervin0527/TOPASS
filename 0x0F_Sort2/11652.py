import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(n)]

    nums.sort()
    count = 1
    max_count = 1
    max_value = nums[0]  # 첫 번째 값으로 초기화

    for idx in range(1, n):  # 첫 번째 요소는 이미 처리했으므로 1부터 시작
        if nums[idx] == nums[idx-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_value = nums[idx-1]
            count = 1  # 새로운 숫자의 등장으로 카운트를 1로 재설정

    # 마지막 숫자 그룹에 대한 처리
    if count > max_count:
        max_value = nums[n-1]

    print(max_value)
