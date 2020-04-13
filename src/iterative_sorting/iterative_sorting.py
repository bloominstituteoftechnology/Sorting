############################################################
#   ITERATIVE SORTING
############################################################

from ..compare import compare_ascending


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr, compare=compare_ascending):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr, compare=compare_ascending):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1, compare=compare_ascending):

    return arr
