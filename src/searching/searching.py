# STRETCH: implement Linear Search
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while (high - low) > 0:
        print(high - low)
        m = (high + low) // 2
        if arr[m] > target:
            high = m - 1
        elif arr[m] < target:
            low = m
        else:
            return m
        if high - low == 1:
            if target == arr[high]:
                return high
            if targed == arr[low]:
                return low
            return -1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if high - low < 1:
        return -1

    m = (high + low) // 2
    if arr[m] > target:
        high = m - 1
    elif arr[m] < target:
        low = m
    else:
        return m

    if high - low == 1:
        if target == arr[high]:
            return high
        if targed == arr[low]:
            return low
        return -1      

    return binary_search_recursive(arr, target, low, high)


arr = [1, 5, 5, 7, 8, 9]
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(arr1, -8, 0, len(arr1) - 1))
