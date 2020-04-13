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

    n = len(array)

    # for each pair of items in _mutating_ array...
    for i in range(1, n):

        item = array[i]  # the item to move
        j = i  # index where item should move to

        # from [j] to the left, swap [j] and [j-1] until correct index for item
        while compare(item, array[j - 1]) < 0 and j > 0:
            array[j] = array[j - 1]
            j -= 1

        # insert item at [j]
        array[j] = item

    return array


# TO-DO: Complete the selection_sort() function below
def selection_sort(array, compare=compare_ascending):
    # 0. take some array
    # 1. imagine the beginning of the array as "sorted" -- currently empty
    # 2. start with the first item (i = 0, 1, 2, ...) -- this is the "current minimum"
    # 3. move through the rest of array and record each value "less" than the "current minimum" as the new "current minimum"
    # 4. swap the "current minimum" with item _after_ the end of the "sorted" portion of array
    # 5. repeat for the remaining "unsorted" portion of array

    n = len(array)  # size of full array

    # for each pair of items in _mutating_ array...
    for i in range(0, n - 1):

        p = i  # index of this iteration's "minimum"

        # find the index of the "minumum" in "unsorted" portion...
        for j in range(i, n):
            if compare(array[j], array[p]) < 0:
                p = j

        # swap
        item = array[p]
        array[p] = array[i]
        array[i] = item

    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(array, compare=compare_ascending):
    # 0. take some array
    # 1. for each pair of items (i, i+1) in the "unsorted" array, compare
    # 2. swap array[i] and array[i+1] if they are out of order
    # -- doing this once will move the "maximum" item to the end of array, which is now "sorted"
    # 3. repeat the process on the "unsorted" array until nothing is left

    n = len(array)  # size of full array

    # for each pair of items in _mutating_ array...
    for i in range(0, n - 1):

        m = n - i  # size of "sorted" portion

        # sort "unsorted" portion...
        for j in range(0, m - 1):
            if compare(array[j + 1], array[j]) < 0:
                # swap
                item = array[j + 1]
                array[j + 1] = array[j]
                array[j] = item

    return array


# STRETCH: implement the Count Sort function below
def count_sort(array, maximum=-1, compare=compare_ascending):

    return array
