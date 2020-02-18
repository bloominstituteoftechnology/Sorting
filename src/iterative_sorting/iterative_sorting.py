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


# Algorithm
# 1. Start with current index = 0
# 2. For all indices EXCEPT the last index:
#     a. Loop through elements on right-hand-side of current index and find the smallest element
#     b. Swap the element at current index with the smallest element found in above loop
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        copied_item = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = copied_item
    return arr


# Algorithm
# 1. Loop through your array
#     Compare each element to its neighbor
#     If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
def bubble_sort(arr):
    did_a_swap = True
    while did_a_swap:
        did_a_swap = False
        for i in range(len(arr) - 1):
            left_side = i
            right_side = i + 1
            if arr[left_side] > arr[right_side]:
                copied = arr[left_side]
                arr[left_side] = arr[right_side]
                arr[right_side] = copied
                did_a_swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
