# STRETCH: implement Linear Search				
def linear_search(arr, target):

  for i, e in enumerate(arr):
    if e == target:
      return i
  return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  high = len(arr)-1
  middle = int(high/2)
  # TO-DO: add missing code
  for i in range(middle):
    if target == arr[middle]:
      return middle
    elif target < arr[middle]:
      middle = int(middle/2)
    else:
      middle += int(middle/2)
    
  return -1 # not found



# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0:
    return -1
  middle = int((low+high)/2)
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if target == arr[middle]:
    return middle
  elif target < arr[middle]:
    return binary_search_recursive(arr[:middle], target, 0, middle)
  else:
    return binary_search_recursive(arr[middle:], target, 0, middle+1)
