# STRETCH: implement Linear Search
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low != high:
        mid = (high - low) // 2 + low
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            high = mid

        if arr[mid] < target:
            low = mid

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0:
        return -1  # array empty

    middle = (low + high) // 2

    if arr[middle] == target:
        return middle

    if arr[middle] > target:
        return binary_search_recursive(arr[:middle], target, low, middle)

    if arr[middle] < target:
        return binary_search_recursive(arr[middle:], target, middle, high)

    raise ValueError(f'Values processed incorrectly: arr:{arr}\n' +
                     f'target: {target} low: {low} high: {high}')
