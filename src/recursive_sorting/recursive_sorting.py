# TO-DO: complete the helper function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    # create pointers for each side, starting at 0.
    # Left and right will only increment once an item is added to merged_arr
    left = 0
    right = 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    # NEED TO MAKE SURE TO CONTINUE TO EMPTY ARRAYS
    # BOTH LEFT AND RIGHT ARRAYS MUST BE EMPTIED FOR IT TO BE FULLY MERGED IN MERGED_ARR
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1
    return merged_arr


a = [1, 3, 4, 5]
b = [2, 9, 7, 8]
c = [2, 9, 7, 8, 3, 5]
# print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION


# def merge_sort(arr):
#     # TO-DO

#     return arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort(c))
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
