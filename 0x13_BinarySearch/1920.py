def binary_search(arr, target):
    st = 0
    en = len(arr) - 1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            en = mid - 1
        else:
            st = mid + 1

    return 0

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    m = int(input())
    targets = list(map(int, input().split()))

    ## 리스트 정렬
    numbers.sort()

    ## 이분 탐색
    results = [binary_search(numbers, target) for target in targets]

    for result in results:
        print(result)