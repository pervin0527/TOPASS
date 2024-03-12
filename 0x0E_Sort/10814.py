import sys
input = sys.stdin.readline

def merge(left, right):
    tmp = []
    lidx = ridx = 0
    while lidx < len(left) and ridx < len(right):
        # 나이를 기준으로 비교할 때 숫자 비교를 수행하도록 수정
        if left[lidx][0] <= right[ridx][0]:
            tmp.append(left[lidx])
            lidx += 1
        else:
            tmp.append(right[ridx])
            ridx += 1

    while lidx < len(left):
        tmp.append(left[lidx])
        lidx += 1

    while ridx < len(right):
        tmp.append(right[ridx])
        ridx += 1

    return tmp

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    n = int(input())
    # 나이를 숫자로 변환하여 accounts 리스트를 생성
    accounts = [input().split() for _ in range(n)]
    for i in range(n):
        accounts[i][0] = int(accounts[i][0])  # 나이를 정수로 변환

    results = merge_sort(accounts)
    for r in results:
        print(r[0], r[1])
