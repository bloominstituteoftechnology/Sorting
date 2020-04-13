############################################################
#   RECURSIVE SORTING
############################################################

import sys
sys.path.append("../")

from compare import compare_ascending


def quick_sort(array, compare=compare_ascending):
    pass


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrayA, arrayB, compare=compare_ascending):
    elements = len(arrayA) + len(arrayB)
    merged_array = [0] * elements
    # TO-DO

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(array, compare=compare_ascending):
    # TO-DO

    return array


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(array, start, mid, end, compare=compare_ascending):
    # TO-DO

    return array


def merge_sort_in_place(array, l, r, compare=compare_ascending):
    # TO-DO

    return array


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def tim_sort(array, compare=compare_ascending):

    return array
