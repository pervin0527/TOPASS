import sys
input = sys.stdin.readline

def max_length_of_lan_cables(cables, N):
    low, high = 1, max(cables)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        count = sum(cable // mid for cable in cables)
        
        if count >= N:
            result = mid  # 최대 길이 갱신
            low = mid + 1
        else:
            high = mid - 1
            
    return result

K, N = map(int, input().split())
cables = [int(input().strip()) for _ in range(K)]

print(max_length_of_lan_cables(cables, N))
