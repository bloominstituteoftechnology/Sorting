# STRETCH: implement Linear Search		
# O(n) linear time, for each item in the list it checks against the target		
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
        return -1

arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = linear_search( arr, 22 )
print(arr)


# STRETCH: write an iterative implementation of Binary Search 
# O(log(n)) 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
      mid = (low + high)
      if arr[mid] < target:
          low = mid + 1
      elif target < arr[mid]:
          high = mid - 1
      else:
          return mid
    

  return -1 # not found

arr = [2,5,9,7,4,1,3,8,6]
arr.sort()
print(arr)
arr = binary_search( arr, 3 )
print(arr)




# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  else:
      binary_search_recursive(middle, target, 0, middle)

arr = [2,5,9,7,4,1,3,8,6]
arr.sort()
print(arr)
arr = binary_search_recursive( arr, 3, 0, len(arr) -1 )
print(arr)

