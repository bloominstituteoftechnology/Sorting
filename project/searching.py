# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i, j in enumerate(arr):
    if j == target:
      return i
  return -1   # not found

# print(linear_search([5,34,2,5,7,3,9,10], 9))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = -1
  high = len(arr)

  # TO-DO: add missing code
  while high - low > 1:
    middle = (low + high) // 2
    print('\nBefore: low: ' + str(low) + ' middle: ' + str(middle) + ' high: ' + str(high))
    if arr[middle] == target:
      return middle
    elif arr[middle] < target:
      low = middle
    else:
      high = middle
    print('\nAfter: low: ' + str(low) + ' middle: ' + str(middle) + ' high: ' + str(high))
  return -1 # not found

# print(binary_search([1, 2, 3, 4, 5, 7, 9, 10, 18, 19], -1561))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low = -1, high = None):
  
  if high == None:
    high = len(arr)

  middle = (low + high) // 2

  # TO-DO: add missing if/else statements, recursive calls
  if target == arr[middle]:
    return middle
  elif high - low <= 1:
    return -1
  elif target < arr[middle]:
    return binary_search_recursive(arr, target, low, middle)
  elif target > arr[middle]:
    return binary_search_recursive(arr, target, middle, high)


  if len(arr) == 0:
    return -1 # array empty

print(binary_search_recursive([1, 2, 3, 4, 5, 7, 9, 10, 18, 19], -513))
