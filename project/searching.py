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
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while high - low > 1:
    middle = low + high // 2
    if middle == target:
      return middle
    elif middle < target:
      low = middle
    else:
      high = middle

  return -1 # not found

print(linear_search([1, 2, 3, 4, 5, 7, 9, 10, 18, 19], 9))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
