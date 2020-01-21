def quicksort(arr):
    return quicksortHelper(arr, 0, len(arr) - 1)


def quicksortHelper(arr, low, high):
    pivotIndex = high

    if low >= high:
        return

    for compareIndex in range(low, high):
        value = arr[compareIndex]
        pivot = arr[pivotIndex]
        if value > pivot:
            arr[compareIndex], arr[pivotIndex] = arr[pivotIndex], arr[compareIndex]
            pivotIndex, compareIndex = compareIndex, pivotIndex
            newPivotIndex = compareIndex - 1
            arr[pivotIndex], arr[newPivotIndex] = arr[newPivotIndex], arr[pivotIndex]
            pivotIndex = newPivotIndex

    quicksortHelper(arr, 0, pivotIndex - 1)
    quicksortHelper(arr, pivotIndex, high)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
quicksort(arr1)
print(arr1)


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
