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
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if low > high:
    return -1
  middle = (low+high)//2

  if(target == arr[middle]):
        return middle
  elif(target < arr[middle]):
        return binary_search_recursive(arr, low, middle -1, target)
  else:
        return binary_search_recursive(arr, middle +1, high, target)

  # TO-DO: add missing if/else statements, recursive calls
