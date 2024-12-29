def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >= 0 and tmp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp
    return a

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    result = insertion_sort(arr)
    print(result)