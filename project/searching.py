# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
# O(log(n))
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  # while loop has runtime of O(log(n)):
    # we are searching through some not all
  while low < high:
    middle = (low + high)/2
    if target < arr[middle]:
      high = middle - 1
    elif target > arr[middle]:
      low = middle + 1
    else:
      return middle

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
# O(log(n))
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if len(arr) == 0:
    return -1 # array empty
  elif low > high:
    return -1
  elif arr[middle] == target:
    return middle
  else:
    if target < arr[middle]:
      high = middle - 1
    else:
      low = middle + 1
    return binary_search_recursive(arr, target, low, high)
