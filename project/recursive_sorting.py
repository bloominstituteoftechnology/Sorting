# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted,
    # we only need to compare the first element of each when merging!
    for i in range(0, elements):
        # all elements in arrA have been merged
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        # next element in arrA smaller, so add to final array
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # else, next element in arrB must be smaller, so add it to final array
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        # split recusively into sinlge el arrays
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # merge() defined later
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# implement the Quick Sort function below
def quick_sort(arr, low, high):
    if len(arr) >= 1:
        # select a pivot element (middle)
        pivot = arr[high // 2]
        lhs = [i for i in arr if i < pivot]
        rhs = [i for i in arr if i > pivot]

        return (quick_sort(lhs, 0, len(lhs)-1) + [pivot] +
                quick_sort(rhs, 0, len(rhs)-1))

    else:
        return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
