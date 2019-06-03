# STRETCH: implement Linear Search
def linear_search(list, target):

  # TO-DO: add missing code
    for i in range(0, len(list)):
        print(list[i], target)
        if list[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(list, target):

    if len(list) == 0:
        return -1  # list empty

    low = 0
    high = len(list)-1

    # TO-DO: add missing code
    while (low + high // 2) < len(list) - 1:
        mid = low + high // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(list, target, low, high):

    middle = (low+high)//2

    if len(list) == 0:
        return -1  # list empty
    # TO-DO: add missing if/else statements, recursive calls
    if target == list[middle]:
        return middle
    elif middle == len(list) - 1:
        return -1
    elif target < list[middle]:
        return binary_search_recursive(list, target, low, middle - 1)
    else:
        return binary_search_recursive(list, target, middle + 1, high)
