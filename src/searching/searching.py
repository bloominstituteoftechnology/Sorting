# implementation of Linear Search				
def linear_search(arr, target):
   for i in range( 0, len(arr) ):
      if arr[i] == target:
         return i
   return -1   # not found


# ITERATIVE implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    middle = (low+high)/2
    if target < arr[middle]:
      high = middle-1 # eliminate RHS
    elif target > arr[middle]:
      low = middle+1 # eliminate LHS
    else:
      return middle

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
