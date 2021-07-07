# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
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
  found = False

  # Loop through array, breaking it up
  while found == False:
    mid = int(high/2)

    # Check middle:
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      # Discard rhs
      high = mid
    else:
      # Discard lhs
      low = mid


  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  
  if arr[middle] == target:
    return middle
  elif arr[middle] > target:
    high = middle
  else:
    low = middle

  return binary_search_recursive(arr, target, low, high)
