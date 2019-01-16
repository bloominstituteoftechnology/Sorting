# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for element in range(len(arr)):
    if arr[element] == target:
      return element
  
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    middle = (low + high) // 2
    
    if arr[middle] == target:
      return middle
    elif arr[middle] > target:  # If target is less than the middle, ignore the right side
      high = middle - 1
    else:
      low = middle + 1
    
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low + high) // 2

  if len(arr) == 0:
    return -1 # array empty
  
  if arr[middle] == target:
    return middle
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle - 1)
  else:
    return binary_search_recursive(arr, target, middle + 1, high)