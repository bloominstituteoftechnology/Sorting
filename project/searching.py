# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for item in arr:
    if item == target:
      return item

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1 

  while low <= high:
    current = (high + low) // 2
    if arr[current] == target:
      return arr[current]
    elif target < arr[current]:
      high = current - 1
    elif target > arr[current]:
      low = current + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
# def binary_search_recursive(arr, target, low, high):
  
#   middle = (low+high)/2

#   if len(arr) == 0:
#     return -1 # array empty
#   # TO-DO: add missing if/else statements, recursive calls

list = [1,2,3,4,5,6,7,8,9,10]
# print(linear_search(list, 1))
# print(linear_search(list, 11))

print(binary_search(list, 1))
print(binary_search(list, 4))
print(binary_search(list, 11))