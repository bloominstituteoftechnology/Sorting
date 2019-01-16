# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    start = 0
    last = len(arr) - 1

    for i in range(len(arr)):
        mid = (start + last) // 2
        if target < arr[mid]:
            last = mid - 1
        else:
            if target == arr[mid]:
                return mid
            else:
                start = mid + 1

    return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) / 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
