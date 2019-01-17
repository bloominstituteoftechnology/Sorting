# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  # simple search idea, return target if it is what you're looking for
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

  # TO-DO: add missing code
  found = False

  while low <= high and not found:
    # split the values to get the middle
    middle = (low + high) // 2

    if arr[middle] == target:
      found = True
    # if the middle value is not the desired value, begin working high and low towards the middle
    else:
      if target < arr[middle]:
        high = middle - 1
      else:
        low = middle + 1

  return found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
