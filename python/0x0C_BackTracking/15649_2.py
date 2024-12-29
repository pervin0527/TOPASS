# def func(m, nums, arr, checks):
#     if len(arr) == m:
#         result = ' '.join([str(x) for x in arr])
#         print(result)
#         return
    
#     for i in range(len(nums)):
#         if checks[i]:
#             arr.append(nums[i])
#             checks[i] = False
#             func(m, nums, arr, checks)
#             arr.pop()
#             checks[i] = True

# def main():
#     N, M = map(int, input().split())
#     numbers = [x for x in range(1, N+1)]
#     checkers = [True] * N
#     func(M, numbers, [], checkers)


# if __name__ == "__main__":
#     main()

def func(m, nums, arr):
    if len(arr) == m:
        result = ' '.join([str(x) for x in arr])
        print(result)
        return
    
    for i in range(len(nums)):
        arr.append(nums[i])
        tmp_nums = nums[:]
        tmp_nums.pop(i)
        func(m, tmp_nums, arr)
        arr.pop()

def main():
    N, M = map(int, input().split())
    numbers = [x for x in range(1, N+1)]
    func(M, numbers, [])


if __name__ == "__main__":
    main()