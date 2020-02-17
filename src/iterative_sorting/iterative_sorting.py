

# Insertion Algorithm
def insertion_sort(arr):
    # 1. Separate the first element from the rest of the array. Think about it as a sorted list of one element.
    # 2. For all other indices, beginning with [1]:
    for i in range(1, len(arr)):
        # a. Copy the item at that index into a temp variable
        copied_item = arr[i]
        # b. Iterate to the left until you find the correct index in the "sorted" part of the array
        # at which this element should be inserted
        j = i
        while j > 0 and copied_item < arr[j - 1]:
            # Shift items over to the right as you iterate
            arr[j] = arr[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        arr[j] = copied_item
    return arr


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
