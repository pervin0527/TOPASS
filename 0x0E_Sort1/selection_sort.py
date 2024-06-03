def selection_sort(a):
    for i in range(len(a)-1):
        min_v_idx = i
        for j in range(i+1, len(a)):
            if a[min_v_idx] > a[j]:
                min_v_idx = j    
        a[i], a[min_v_idx] = a[min_v_idx], a[i]
        
    return a
            

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    result = selection_sort(arr)
    print(result)