# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target:
      return 1

  return -1   # not found



# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  arr.sort() # arr must be sorted for Binary Search
    
  while len(arr) > 0:
    pivot_index = int( len(arr) / 2 )
    pivot = arr[pivot_index]

    if pivot == target:
      return 1
    
    elif pivot > target:
      arr = arr[:pivot_index]
    
    else:
      arr = arr[pivot_index + 1:]

  return -1 # not found



# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target):
  
  if len(arr) == 0:
    return -1 # array empty
  
  arr.sort() # in production I would sort the list before passing to the recursive function so that I didn't sort a sorted list, but, hey, this is a first pass solution

  pivot_index = int( len(arr) / 2 )
  pivot = arr[pivot_index]

  if pivot == target:
    return 1

  elif pivot < target:
    return binary_search_recursive(arr[pivot_index + 1:], target)
  
  else:
    return binary_search_recursive(arr[:pivot_index], target)

print(binary_search_recursive([1, -1, 5, 6, 8, 2, 4, 5], 1))
