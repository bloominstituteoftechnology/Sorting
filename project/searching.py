# STRETCH: implement Linear Search				
def linear_search(arr, target):
    
  # TO-DO: add missing code
    if len(arr) == 0: 
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i # target value Found at index position i

    return -1   # not found

arr = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print(linear_search(arr, -6))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1
    # TO-DO: add missing code
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid
            continue
        elif arr[mid] < target:
            low = mid
            continue

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
