############################################################
#   ITERATIVE SORTING
############################################################

import sys
sys.path.append("../")

from compare import compare_ascending


def insertion_sort(array, compare=compare_ascending):
    # 0. take some array
    # 1. start with the first item (i = 0) in the array -- this is sorted
    # 2. take array[i], the next item (i = 1, 2, ...) in the array
    # 3. compare array[i] to each previous item (j = i, i-1, ...) until you find the right spot for array[i]
    # 4. move all checked items "more" than array[i] to the right and insert array[i] at its new index in the "sorted" portion of the array
    # 5. repeat until there are no more items to sort

    # for each item in _mutating_ array
    for i in range(1, len(array)):

        item = array[i]
        j = i  # this index moves

        # from [j] to the left, swap [j] and [j-1] until correct index for item
        while compare(item, array[j - 1]) < 0 and j > 0:
            array[j] = array[j - 1]
            j -= 1

        # insert item at [j]
        array[j] = item

    return array


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
