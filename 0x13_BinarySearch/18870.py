def binary_search(n, arr):
    start = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    
    ## 정렬
    arr1 = numbers[:]
    arr1.sort()

    ## 중복제거
    arr2 = []
    for i in range(n):
        number = arr1[i]
        if i == 0:
            arr2.append(number)
        
        if i > 0 and arr1[i] != arr1[i-1]:
            arr2.append(number)

    ## 이분탐색
    result = [binary_search(x, arr2) for x in numbers]
    print(' '.join([str(x) for x in result]))