# TO-DO: Complete the selection_sort() function below
# 2 loops, second staring at i + 1 thru array
#  keep track of minimum value
# to initialize we'll set smallest value to the first item
# if the element is smaller than the minimum value
# then that element becomes the minimum, swap their positions


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # TO-DO: swap

    return arr


print(selection_sort([2, 3, 5, 8, 7, 1, 4]))

# TO-DO:  implement the Bubble Sort function below
# loop through array
# compare item with item next to it
# if item is greater than item next to it, swap items


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([2, 7, 6, 8, 3, 4, 1]))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
