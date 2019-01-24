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
    middle = int((low + high)/2)
    if target > arr[middle]:
      low = middle
    elif target < arr[middle]:
      high = middle
    else:
      print(middle)
      return middle

  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = int((low+high)/2)

  if len(arr) == 0:
    return -1
  elif arr[middle] > target:
    return binary_search_recursive(arr[:middle], target, 0, middle)
  elif arr[middle] < target:
    return binary_search_recursive(arr[middle:], target, middle, len(arr) - 1)
  else:
    return middle