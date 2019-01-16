# STRETCH: implement Linear Search	
an_array = [4, 6, 7, 3, 1, 3030, 99, 2000]			
def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  
  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    middle = (low+high)//2
    if target < arr[middle]:
      high = middle - 1
    elif target > arr[middle]:
      high = middle + 1
    else:
      return middle
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  while low<=high:
    if target < arr[middle]:
      return binary_search_recursive(arr, target, low, middle - 1)
    elif target > arr[middle]:
      return binary_search_recursive(arr, target, low, middle + 1)
    else:
      return middle
  # TO-DO: add missing if/else statements, recursive calls
print(binary_search_recursive(an_array, 7, 0, len(an_array) - 1))