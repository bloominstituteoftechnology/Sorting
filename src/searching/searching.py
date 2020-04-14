# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  # iterate over the arr
  for idx in range(len(arr)):
    # if el at index is uqual to target
    if arr[idx] == target:
      # return index
      return idx
  # if element is not present, return -1
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  # assign a starting and ending point
  low = 0
  high = len(arr)-1
  # assign a middle
  mid = len(arr) // 2

  # if the element is not present return -1 
  if len(arr) == 0:
    return -1 # array empty

  # TO-DO: add missing code
  # iterate while mid el is not target, and while low index is not equal to high
  while(arr[mid] != target and low != high):
    # if target is smaller than el in list at mid point
    if(target < arr[mid]):
      # move high to mid - 1
      high = mid - 1
      # else move low to mid + 1
    else:
      low = mid + 1

    # change middle to new based on array length
    mid = (low + high) // 2

  # if mid is target el than return index
  if(arr[mid] == target):
    return mid

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
