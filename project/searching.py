# STRETCH: implement Linear Search
def linear_search(arr, target):
    # iterate over a list
    for i, item in enumerate(arr):
        # check if each item matches target
        if item == target:
            return i

    # if not found
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    # array empty
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr)-1

    while low <= high:
        # find middle
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            hight = middle - 1
        elif target > arr[middle]:
            low = middle + 1

    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)/2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
