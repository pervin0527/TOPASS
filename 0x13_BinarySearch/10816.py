def binary_search(numbers, target):
    cnt = 0
    isin = True
    while isin:
        start = 0
        end = len(numbers) - 1
        numbers.sort()

        is_find = False
        while start <= end:
            mid = (start + end) // 2

            if numbers[mid] == target:
                cnt += 1
                is_find = True
                numbers[mid] = 10000001

            elif numbers[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        if not is_find:
            isin = False
    
    return cnt


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    m = int(input())
    targets = list(map(int, input().split()))

    result = [binary_search(numbers, target) for target in targets]
    result = ' '.join([str(x) for x in result])
    print(result)