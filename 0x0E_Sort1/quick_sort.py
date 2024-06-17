def quick_sort(arr, start, end):
    """
    현재 입력된 배열의 시작 위치와 끝 위치.
    """
    if start < end:
        pi = partition(arr, start, end) ## pi는 pivot의 적절한 위치(idx)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)

def partition(arr, low, high):
    pivot = arr[low]  # 첫 요소를 피벗으로 선택
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right >= left and arr[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap
            arr[left], arr[right] = arr[right], arr[left]

    # 피벗을 올바른 위치에 놓기
    arr[low], arr[right] = arr[right], arr[low]

    return right

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)