# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for element in arr:
    if element == target:
      return element

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  low = 0
  high = len(arr)-1
  notfound = True
  while notfound:
    middle = int((low+high)/2)
    if target == arr[middle]:
      return middle
    elif target < arr[middle]:
      high = middle - 1

    elif target > arr[middle]:
      low = middle + 1
    else:
      notfound = False
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2

  if len(arr) > 2:
    return -1 

  if target == arr[middle]:
    return arr[middle]
  if target < arr[middle]:
    low = middle -1
  if target > arr[middle]:
    high = middle + 1
  
  return binary_search_recursive(arr[low:high], target, low, high)