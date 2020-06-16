# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    merged_index = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] > arrB[j]:
            merged_arr[merged_index] = arrB[j]
            j += 1

        elif arrA[i] < arrB[j]:
            merged_arr[merged_index] = arrA[i]
            i += 1

        merged_index += 1

    merged_arr = merged_arr[:merged_index]
    if i < len(arrA):
        merged_arr.extend(arrA[i:])
    if j < len(arrB):
        merged_arr.extend(arrB[j:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid_index = math.floor(len(arr)/2)
    left = arr[:mid_index]
    right = arr[mid_index:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    arr = merge(left_sorted, right_sorted)
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
