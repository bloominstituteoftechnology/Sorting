# STRETCH: implement Linear Search	
# 
# 
# 			
import math
def linear_search(arr, target):
  for index, i in enumerate(arr):
    if i == target:
      return index
  return -1

print(linear_search([1, 2, 3, 4, 5], 4))


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  max_iter = math.log(len(arr), 2)
  for _ in range(int(math.ceil(max_iter))):    
    mid = (high + low) // 2
    # TO-DO: add missing code
    if arr[mid] == target:
      return mid
    else:
      if arr[mid] < target:
        low = mid
      else:
        high = mid

  return -1 # not found


print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
