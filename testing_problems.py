def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


arr = [2, 5, 3, 1, 9]
print(insertion_sort(arr))
