# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    
    if len(arr) == 0:
        return -1 # array empty

    low = 0
    high = len(arr)

    # TO-DO: add missing code
    while high > low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid
        elif arr[mid] < target:
            low = mid + 1
    

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    mid = (low + high) // 2
    if len(arr) == 0:
      return -1 # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[mid] == target:
         return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
