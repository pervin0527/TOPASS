import sys
input = sys.stdin.readline

def merge(larr, rarr):
    tmp = []
    lidx = ridx = 0
    while lidx < len(larr) and ridx < len(rarr):
        if larr[lidx][0] < rarr[ridx][0]:
            tmp.append(larr[lidx])
            lidx += 1

        elif larr[lidx][0] == rarr[ridx][0]:
            if larr[lidx][1] <= rarr[ridx][1]:
                tmp.append(larr[lidx])
                lidx += 1
            else:
                tmp.append(rarr[ridx])
                ridx += 1

        else:
            tmp.append(rarr[ridx])
            ridx += 1

    while lidx < len(larr):
        tmp.append(larr[lidx])
        lidx += 1

    while ridx < len(rarr):
        tmp.append(rarr[ridx])
        ridx += 1

    return tmp


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)


if __name__ == "__main__":
    n = int(input())
    coords = [list(map(int, input().split())) for _ in range(n)]

    result = merge_sort(coords)
    for res in result:
        print(" ".join(map(str, res)))