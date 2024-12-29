def lower_idx(target, l):
    st = 0
    en = l

    while st < en:
        mid = (st + en) // 2
        if numbers[mid] >= target:
            en = mid
        else:
            st = mid + 1
    
    return st

def upper_idx(target, l):
    st = 0
    en = l

    while st < en:
        mid = (st + en) // 2
        if numbers[mid] > target:
            en = mid
        else:
            st = mid + 1

    return st

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        print(upper_idx(target, n) - lower_idx(target, n), end=" ")