# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    mid = (low + high) // 2

    while low < high:
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid
            mid = (low + high) // 2
        else:
            low = mid + 1
            mid = (low + high) // 2

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty

    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle)
    else:
        return binary_search_recursive(arr, target, middle + 1, high)
