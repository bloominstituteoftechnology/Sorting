# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0  # indicies for keeping track
    b = 0
    # TO-DO
    for value in range(0, elements):
        if a >= len(arrA):  # occurs when all elements in array A have been merged
            merged_arr[value] = arrB[b]
            b += 1
        elif b >= len(arrB):  # occurs when all elements in array B have been merged
            merged_arr[value] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]: # occurs if the element at the current index of array A is less than that of array B
            merged_arr[value] = arrA[a]
            a += 1
        else: # occurs if the element at the current index of array B is less than that of array A
            merged_arr[value] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # Divide the array and assign both halves
        mid = len(arr)//2
        # Recursively split each side until there is only one element
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # Merge the two sides together
        arr = merge(left, right)
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
