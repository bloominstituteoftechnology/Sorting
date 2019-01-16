# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in arr:
        if i == target:
            return i

    return -1   # not found


print('Linear:', linear_search([1, 2, 3], 3))
# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high >= low:

        middle = round((high+low)/2)
        if arr[middle] == target:
            return arr[middle]
        elif arr[middle] > target:
            high = middle + 1
        elif arr[middle] < target:
            low = middle + 1
    return -1  # not found


print('Binary:', binary_search([1, 2, 3, 4, 5, 6], 5))
# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target):

    middle = round(len(arr)/2)

    if arr[middle] == target:
        return arr[middle]
    if len(arr) == 1:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    elif arr[middle] > target:
        arr = arr[:middle]
    elif arr[middle] < target:
        arr = arr[middle:]

    return binary_search_recursive(arr, target)


print('Binary Recursive:', binary_search_recursive([1, 2, 3, 4, 5, 6], 0))
