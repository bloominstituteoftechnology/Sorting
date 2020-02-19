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
    max_loops = len(arr) + 1
    num_of_loops = 1
    while num_of_loops < max_loops:
        midpoint = (low + high) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            low = midpoint
        else:
            high = midpoint
        num_of_loops += 1


def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2
    if len(arr) == 0:
        return -1  # array empty
    elif arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle, high)
    else:
        return binary_search_recursive(arr, target, low, middle)
