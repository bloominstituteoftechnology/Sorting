# STRETCH: implement Linear Search		
# O(n) linear time, for each item in the list it checks against the target		
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index

arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = linear_search( arr, 8 )
print(arr)


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
