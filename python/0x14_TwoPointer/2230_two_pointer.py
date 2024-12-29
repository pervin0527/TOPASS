import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [int(input().strip()) for _ in range(n)]
    arr.sort()
    
    right = 0
    min_diff = float('inf')
    for left in range(n - 1):
        while right < n and arr[right] - arr[left] < m:
            right += 1
        if right < n:
            min_diff = min(min_diff, arr[right] - arr[left])
    
    print(min_diff)