def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

if __name__ == "__main__":
    arr = [9, 1, 6, 8, 4, 3, 2, 0]
    result = bubble_sort(arr)
    print(result)