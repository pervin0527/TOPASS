## 선택정렬(selection sort)
arr = [9, 1, 6, 8, 4, 3, 2, 0]

for i in range(len(arr)):
    min_idx = i
    ## 최소값 탐색.
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    
    ## 원소간 위치 전환.    
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)