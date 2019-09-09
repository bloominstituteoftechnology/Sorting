# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in arr:
        if arr[i] == target:
            return i


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    middle = len(arr)/2
    found = 0
    while found == 0:
        if middle == target:
            found = 1
        elif middle > target:
            middle = len(arr[:middle-1])/2
        else:
            middle = len(arr[middle+1:])/2

    return middle  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
