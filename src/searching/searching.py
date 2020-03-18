# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range( 0, len(arr) ):
    if arr[i] == target:
      return i
  return -1  

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
  return None
  return -1 # not found (an intended error) 


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  mid = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  elif low > high:
    return -1 # not found
  if arr[int(mid)] == target: 
    return mid 
          
  # if our middle element is greater than our search value
  # look at the lower subsection
  elif arr[int(mid)] > target: 
    high = mid - 1
  # if our middle element has not been found and not greater than our search value
  # look at the upper or subsection with bigger values
  else:
    low = mid + 1 

  # TO-DO: add missing if/else statements, recursive calls
  return binary_search_recursive(arr, target, low, high)
