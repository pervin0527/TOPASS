import sys
input = sys.stdin.readline

def binary_search(target, arr):
    st, en = 0, len(arr)-1
    
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            st = mid + 1
        elif  arr[mid] > target:
            en = mid - 1
    
    return False
        
def solution1():
    N = int(input())
    A = list(map(int, input().rstrip().split()))

    M = int(input())
    B = list(map(int, input().rstrip().split()))

    ## A를 정렬
    A.sort()

    ## A에 b가 존재하는지 하나씩 검사.
    result = []
    for b in B:
        if binary_search(b, A):
            result.append(1)
        else:
            result.append(0)

    result = '\n'.join(map(str, result))
    print(result)
        
if __name__ == "__main__":
    solution1()