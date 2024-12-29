def counting_sort(arr):
    # 배열에서 최소값과 최대값 찾기
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    # 카운트 배열 초기화
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # 카운트 배열에 각 요소의 발생 횟수 저장
    for number in arr:
        count[number - min_val] += 1

    # 카운트 배열 업데이트 (누적 합 계산)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 결과 배열을 빌드 (뒤에서부터 시작하여 안정적인 정렬 보장)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # 원본 배열을 결과 배열로 업데이트
    for i in range(len(arr)):
        arr[i] = output[i]

arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Sorted array is:")
for i in arr:
    print("%d" % i, end=" ")
