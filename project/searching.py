# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # returns position of the target found

    return -1  # not found


print(linear_search([3, 4, 1, 2], 2))

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


print(binary_search([5, 6, 7, 8, 10], 10))

# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    if arr[middle] > target:
        if high >= 0:
            return binary_search_recursive(arr, target, low, middle - 1)

        return -1
    else:
        if low >= 0:
            return binary_search_recursive(arr, target, middle + 1, high)

        return -1


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(arr1, -8, 0, len(arr1) - 1))

