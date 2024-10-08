def merge(left, right):
    result = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
        
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
        
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


if __name__ == "__main__":
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    
    result = merge_sort(numbers)
    for num in result:
        print(num)


# def main():
#     N = int(input().rstrip())
#     arr = [int(input().rstrip()) for _ in range(N)]

#     arr.sort()
#     result = "\n".join([str(x) for x in arr])
#     print(result)

# if __name__ == "__main__":
#     main()