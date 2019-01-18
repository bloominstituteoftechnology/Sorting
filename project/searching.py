# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # TO-DO: add missing code
  for i, a in enumerate(arr):
    if a == target:
      return i
    else:
      pass
  return -1

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    p = (low+high) // 2
    if arr[p] == target:
      return p
    elif arr[p] < target:
      low = p + 1
    else:
      high = p - 1

  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
# def binary_search_recursive(arr, target, low=0, high=len(arr)):
  
#   middle = (low+high)//2

#   if len(arr) == 0:
#     return -1 # array empty
#   # TO-DO: add missing if/else statements, recursive calls
#   if arr[middle] == target:
#     return middle
#   elif arr[middle] < target:
#     low = middle + 1
#     binary_search_recursive(arr, target, low, high)
#   elif arr[middle] > target:
#     high = middle - 1
#     binary_search_recursive(arr, target, low, high)

# print(binary_search_recursive([1,2,3,4,5,6,7,8,9,10], 2)