def solution(nums, tmp):
    if len(tmp) == M:
        total.append(tmp)
        return

    for num in nums:
        new_nums = nums[:]
        new_nums.remove(num)
        solution(new_nums, tmp + [num])


N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]

tmp = []
total = []
solution(numbers, tmp)

for permutations in total:
    for number in permutations:
        print(number, end=" ")
    print()