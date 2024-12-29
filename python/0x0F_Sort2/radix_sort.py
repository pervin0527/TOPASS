def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # 정렬된 배열을 저장할 공간
    count = [0] * 10  # 0~9까지 각 숫자의 개수를 저장할 배열

    # 현재 자릿수(exp)에 따른 숫자의 개수를 count 배열에 저장
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # count 배열을 수정하여, count[i]가 실제로 출력 배열에 i가 위치해야 하는 첫 번째 인덱스를 가리키도록 함
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 출력 배열을 빌드
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # arr[]를 수정하여 정렬된 숫자를 포함하도록 함
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # arr에서 가장 큰 수 찾기
    max_val = max(arr)

    # 모든 자릿수에 대해 counting_sort를 수행
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)