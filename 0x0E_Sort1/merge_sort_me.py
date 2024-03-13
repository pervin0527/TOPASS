def merge(arr, left_half, right_half):
    i = j = k = 0

    # 왼쪽과 오른쪽 부분 배열을 비교하면서 병합
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # 왼쪽 부분 배열에 남은 요소들을 결과 배열에 추가
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # 오른쪽 부분 배열에 남은 요소들을 결과 배열에 추가
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr):
    """
    [중요] 반드시 디버깅을 해볼 것. 아래쪽 화살표(단계정보, F11)을 수행하면 전체 과정을 알 수 있다.
    
    배열의 길이가 1이 되면, 해당 배열은 이미 정렬되어 있다고 볼 수 있으므로 더 이상의 분할 없이 병합 과정으로 넘어간다.
    쉽게 말해 길이가 1이 되면 if문에 해당하지 않으므로 arr의 길이가 1일 때 merge_sort는 return만 수행.
    다시 merge_sort(len(arr) = 2)로 돌아오면 left와 right는 각각 원소가 한 개인 배열이고 merge 함수로 전달된다.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(arr, left, right)


if __name__ == "__main__":
    arr = [6, -8, 1, 12, 8, 15, 7, -7]
    merge_sort(arr)
    print(arr)