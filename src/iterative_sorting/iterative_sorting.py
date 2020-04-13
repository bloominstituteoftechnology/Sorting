############################################################
#   ITERATIVE SORTING
############################################################

from ..compare import compare_ascending


# TO-DO: Complete the selection_sort() function below
def selection_sort(array, compare=compare_ascending):
    # loop through n-1 elements
    for i in range(0, len(array) - 1):
        current_index = i
        index_of_min = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(array, compare=compare_ascending):

    return array


# STRETCH: implement the Count Sort function below
def count_sort(array, maximum=-1, compare=compare_ascending):

    return array
