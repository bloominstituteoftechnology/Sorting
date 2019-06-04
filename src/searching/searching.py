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
  high = len(arr)-1

  while high - low > 0:
    mid = (high + low) // 2
    if arr[mid] == target:
      return mid
    elif target > arr[mid]:
      low = mid
    else:
      high = mid
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0:
    return -1 # array empty

  middle = (low+high)//2

  if high - low == 0:
    return -1 # not found
  if arr[middle] == target:
    return middle
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle, high)
  else:
    return binary_search_recursive(arr, target, low, middle)
