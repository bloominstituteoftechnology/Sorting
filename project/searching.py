# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for element in arr:
    if element == target:
      return element 
  return -1   # not found
  
  # for i in range (0, len(arr)): 
  #   if (arr[i] == target): 
  #     return arr[i]; # returns the value if found
  # return -1
print(f'This is linear search {linear_search([1, 4, 6, 8], 6)}')
# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    mid = (low + high)/2 # middle element index
    guess = arr[mid] # middle element 
    if guess == target: #middle element is target
      return mid # return middle element index
    if guess > target:
      high = mid - 1 
      #change the end Index to start from middle - 1 b/c you checked middle already
    else:
      low = mid + 1  
      #change the start Index to start from middle + 1

  return -1 # not found
print(f'This is index of the target for binary search {binary_search([1, 4, 6, 8], 6)}')  

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
