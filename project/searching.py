# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for element in arr:
    if element == target:
      return element

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)

  while len(low,high) > 0:
    middle = int(low+high/2)
    if target == arr[middle]:
      return arr[middle]

    if target < arr[middle]:
      low = middle - 1

    if target > arr[middle]:
      high = middle + 1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if target == arr[middle]
    return arr[middle]
  if target < arr[middle]:
    low = middle -1
  if target > arr[middle]:
    high = middle + 1
  
  return binary_search_recursive(arr[low:high], target, low, high)