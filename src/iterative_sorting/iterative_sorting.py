# v1
# Selection sort:
# 1. set the current_minimum to the first item
# 2. compare each current_item in list to the current_minimum
# - find the lowest smaller number and swap that current_item
# with the current_minimum
# 3. repeat

# e.g.
# arr = [67,31,24,11,72,42,37,99,75]

# selection_sort() function


def selection_sort(arr):
    # we will be comparing to see which number is smaller
    # switcing the numbers when a smaller number is found
    # loop through n-1 elements
    # but not running the same process on the last index location
    for array_index_1 in range(0, len(arr) - 1):
        # comparing each index to those that follow
        for current_index in range(array_index_1 + 1, len(arr) - 1):

            # if the current_index is smaller than the array_index_1
            if arr[current_index] < arr[array_index_1]:
                # store the value that is located at array_index_1
                swap_memory_value = arr[array_index_1]

                # replace array_index_1's value with that of the current_index
                arr[array_index_1] = arr[current_index]

                # replace current_index's value with
                # the stored array_index_1 in swap_memory
                arr[current_index] = swap_memory_value

    return arr


# TO-DO:  implement the Bubble Sort function below
# Bubble Sort:
# -1 compare 1,2, then 2,3 until end of list
# -2 for each comparison, put the smallest first
# -3 keep track of changes
# -4 repeat until there are no changes

# e.g.
# arr = [6,3,6,3,7,4,37,9,7]
# the Bubble Sort function
def bubble_sort(arr):

    # outer loop:
    # seeing if changes were made by sort-pass
    changed_by_sort_counter = 1
    while changed_by_sort_counter > 0:

        # tracking location in list index (sequence)
        # track where you are as you iterate through the list
        list_index_counter = 0

        # inner while: comparing ~each number to the next
        # doing one pass through the list
        while list_index_counter < (len(arr) - 1):

            # store the two values
            compare_1 = arr[list_index_counter]
            compare_2 = arr[list_index_counter + 1]

            # resetting changed-by-sort counter
            changed_by_sort_counter = 0

            # if the second number is
            # bigger than the first, then...
            if compare_1 > compare_2:
                # ...swap the numbers
                arr[list_index_counter] = compare_2
                arr[list_index_counter + 1] = compare_1
                # and incriment the change counter
                changed_by_sort_counter += 1

            list_index_counter += 1

    return arr


bubble_sort(arr)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
