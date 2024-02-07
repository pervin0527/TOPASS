"""
Merge Sort
"""

n = 10
arr = [15, 25, 22, 357, 16, 23, -53, 12, 46, 3]
tmp = [0] * 1000001  # merge 함수에서 사용할 임시 배열

def merge(st, en):
    mid = (st + en) // 2
    lidx, ridx = st, mid
    for i in range(st, en):
        if ridx == en:
            tmp[i] = arr[lidx]
            lidx += 1
        elif lidx == mid:
            tmp[i] = arr[ridx]
            ridx += 1
        elif arr[lidx] <= arr[ridx]:
            tmp[i] = arr[lidx]
            lidx += 1
        else:
            tmp[i] = arr[ridx]
            ridx += 1
    for i in range(st, en):
        arr[i] = tmp[i]  # 임시 배열에 저장된 값을 원래 배열로 복사

def merge_sort(st, en):
    if en == st + 1:  # 배열의 길이가 1이면 정렬하지 않고 반환
        return
    mid = (st + en) // 2
    merge_sort(st, mid)  # 왼쪽 부분 배열 정렬
    merge_sort(mid, en)  # 오른쪽 부분 배열 정렬
    merge(st, en)  # 두 부분 배열을 합치면서 정렬

# 병합 정렬 실행
merge_sort(0, n)

# 정렬된 배열 출력
for i in range(n):
    print(arr[i], end=' ')
