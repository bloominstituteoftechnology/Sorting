
# helper function


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

# additonal way to write handle function


def merge(arrA, arrB):
    a = 0
    b = 0
    merge_array = []
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merge_array.append(arrA[a])
            a += 1
        elif arrA[a] > arrB[b]:
            merge_array.append(arrB[b])
            b += 1
        else:
            merge_array.append(arrA[a])
            merge_array.append(arrB[b])
            a += 1
            b += 1

    while a < len(arrA):
        merge_array.append(arrA[a])
        a += 1

    while b < len(arrB):
        merge_array.append(arrB[b])
        b += 1

    return merge_array

# recursive sorting function


def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return []
    left = []
    right = []
    pivot = arr[low]
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
    return quick_sort(left, 0, len(left)-1) + [pivot] + quick_sort(right, 0, len(right)-1)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
