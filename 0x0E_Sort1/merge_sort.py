def merge(left, right):
    # 병합 결과를 저장할 리스트 초기화
    sorted_list = []
    i = j = 0
    
    # 두 리스트를 병합하면서 정렬
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 등호를 포함하여 안정성을 보장
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # 남은 요소를 결과 리스트에 추가
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def merge_sort(arr):
    # 배열의 길이가 1 이하이면 그대로 반환 (종료 조건)
    if len(arr) <= 1:
        return arr
    
    # 배열을 두 개의 하위 배열로 분할
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 하위 배열을 재귀적으로 정렬
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 정렬된 하위 배열을 병합
    return merge(left_sorted, right_sorted)

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    result = merge_sort(arr)
    print("Sorted array is:", result)
