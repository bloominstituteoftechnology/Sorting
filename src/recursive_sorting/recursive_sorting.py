############################################################
#   RECURSIVE SORTING
############################################################

from ..compare import compare_ascending


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, compare=compare_ascending):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr, compare=compare_ascending):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end, compare=compare_ascending):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r, compare=compare_ascending):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def tim_sort(arr, compare=compare_ascending):

    return arr
