def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

min_diff = float('inf')
for i in range(n):
    target = arr[i] + m
    j = binary_search(arr, target)
    if j < n:
        min_diff = min(min_diff, arr[j] - arr[i])

print(min_diff)