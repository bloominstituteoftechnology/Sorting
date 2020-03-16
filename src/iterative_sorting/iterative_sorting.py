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


# selection_sort() function
def selection_sort(arr):
    # we will be comparing to see which number is smaller
    # switcing the numbers when a smaller number is found
    # loop through n-1 elements
    # but not running the same process on the last index location
    for array_index_1 in range(0, len(arr) - 1):
        # comparing each index to those that follow
        for current_index in range(array_index_1 + 1, len(arr)):

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


# Bubble Sort:
# -1 compare 1,2, then 2,3 until end of list
# -2 for each comparison, put the smallest first
# -3 keep track of changes
# -4 repeat until there are no changes

# arr = [6,3,6,3,7,4,37,9,7]

# TO-DO: implement the Bubble Sort function below
def bubble_sort(arr):

    # outer loop:
    # Keep sorting as long as changes are being made
    # check if changes were made by sort-pass
    # changed_by_sort_counter = True
    # while changed_by_sort_counter == True:
    for i in range(len(arr)):

        # tracking location in list index (sequence)
        # track where you are as you iterate through the list
        list_index_counter = 0

        # inner while: comparing ~each number to the next
        # doing one pass through the list
        # (adjust for counting from zero in index vs. length)
        while list_index_counter < (len(arr) - 1):

            # store the two values to compare
            compare_value_1 = arr[list_index_counter]
            compare_value_2 = arr[list_index_counter + 1]

            # resetting changed-by-sort counter to default
            # changed_by_sort_counter = False

            # if the first number is
            # bigger than the second, then...
            if compare_value_1 > compare_value_2:
                # ...swap the numbers
                arr[list_index_counter] = compare_value_2
                arr[list_index_counter + 1] = compare_value_1
                # update change counter
                # changed_by_sort_counter = True

            list_index_counter += 1

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#
#     return arr
