# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for idx, item in enumerate(arr):
    if item == target:
      return idx
    #end of conditional 
  #end of for loop 

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  """
  should take in a sorted array.  time complexity O(log n)
  """
  if len(arr) == 0:
    return -1 # array empty
  
  low = 0
  high = len(arr)-1

  pivot = (low + high) // 2

  while True:
    if target == arr[pivot]:
      return pivot
    elif target < arr[pivot]:
      low = 0
      high = pivot-1
      pivot = (low + high) // 2
    elif target > arr[pivot]:
      low = pivot + 1
      high = len(arr)
      pivot = (low + high) // 2

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  """
  should take in a sorted array.  time complexity O(log n)
  uses recursion
  """

  middle = (low + high)// 2

  if len(arr) == 0:
    return -1 # empty array 
  
  if target == arr[middle]:
    return middle
  elif target < arr[middle]:
    return binary_search_recursive(arr, target, 0, middle -1)
  elif target > arr[middle]:
    return binary_search_recursive(arr, target, middle + 1, len(arr))
