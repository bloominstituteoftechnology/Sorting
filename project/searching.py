# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in arr:
        if i == target:
            return 1

    return -1   # not found


print(linear_search([1, 2, 3], 3))
print(linear_search([1, 2, 3], 4))
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


print(binary_search([1, 2, 3, 4, 5, 6], 50))
# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)/2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
