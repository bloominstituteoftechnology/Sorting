def linear_search(arr, target):
    for it in arr:
        if it == target:
            return arr.index(it)
    return -1  # not found


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    low = 0
    high = len(arr) - 1
    while True:
        midpoint = (low + high) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            low = midpoint
        else:
            high = midpoint


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
