# STRETCH: implement Linear Search				
def linear_search(arr, target):
  if arr == []:
    return -1
  # TO-DO: add missing code
  for i in range(0, len(arr)):
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
  while low <= high:
    middle = (low + high)/2
    if target > arr[int(middle)]:
      low = int(middle)
    elif target < arr[int(middle)]:
      high = int(middle)
    else:
      print(int(middle))
      return int(middle)

  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1
  elif arr[int(middle)] > target:
    return binary_search_recursive(arr[:int(middle)], target, 0, int(middle))
  elif arr[int(middle)] < target:
    return binary_search_recursive(arr[int(middle):], target, int(middle), len(arr) - 1)
  else:
    return int(middle)