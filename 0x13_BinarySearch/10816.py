import sys
input = sys.stdin.readline

def binary_search(arr, target):
    st, en = 0, len(arr)-1
    while st <= en:
        mid = (st + en) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            st = mid + 1
        elif arr[mid] > target:
            en = mid - 1

    return False
        
def solution1():
    N = int(input())
    A = list(map(int, input().rstrip().split()))
    A.sort()

    M = int(input())
    B = list(map(int, input().rstrip().split()))

    dict_a = {}
    for a in A:
        if a in dict_a:
            dict_a[a] += 1
        else:
            dict_a[a] = 1

    results = []
    for target in B:
        if binary_search(A, target):
            results.append(dict_a[target])
        else:
            results.append(0)

    results = ' '.join(map(str, results))
    print(results)

        
if __name__ == "__main__":
    solution1()