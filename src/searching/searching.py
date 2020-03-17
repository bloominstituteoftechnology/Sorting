# STRETCH: implement Linear Search
def linear_search(arr, target):
  for x in range(len(arr)):
        if arr[x] == target:
              return x
  return -1
  # TO-DO: add missing code



import random
# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  x = random.randint(low,high)
  unfound = True
  while unfound:
        unfound = False
        if arr[x] == target:
              return x
        elif arr[x] > target:
              high = x
              x = random.randint(low,high)
              unfound = True
        elif arr[x] < target:
              low = x
              x = random.randint(low,high)
              unfound = True

  return -1 # not found
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1,5))
# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

  middle = (low+high)//2
  if len(arr) == 0:
        return -1 # array empty
  if arr[middle] == target:
        return middle
  elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle-1)
  elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle+1, high)

  # TO-DO: add missing if/else statements, recursive calls
