import sys

def binary_search(i_idx, j_value, sorted_arr):
    st, en = 0, len(sorted_arr) - 1

    while st <= en:
        mid = (st + en) // 2
        if sorted_arr[mid][1] == j_value:
            if sorted_arr[mid][0] > i_idx:
                return True
            else:
                return False

        if sorted_arr[mid][1] < j_value:
            st = mid + 1
        elif sorted_arr[mid][1] > j_value:
            en = mid - 1

    return False


def solution():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    x = int(sys.stdin.readline().strip())

    arr = list(enumerate(arr))
    arr_sorted = sorted(arr, key=lambda x : x[1])

    count = 0
    for i in range(n):
        ai = arr[i] ## (idx, value)

        aj = x - ai[1]
        if binary_search(ai[0], aj, arr_sorted):
            count += 1

    print(count)


if __name__ == "__main__":
    solution()