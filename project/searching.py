# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for item in arr:
    if item == target:
      return item
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
    mid = int((low+high)/2)
    print('high',arr[high])
    print('mid', arr[mid])
    print('low', arr[low])
    if arr[mid] == target:
      print('found it!')
      return arr[mid]
    elif target > arr[mid]:
      low = mid+1
    elif target < arr[mid]:
      high = mid-1


  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  mid = int((low+high)/2)
  print('high',arr[high])
  print('mid', arr[mid])
  print('low', arr[low])
  

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[mid] == target:
    return target
  elif target > arr[mid]:
    binary_search_recursive(arr, target, mid+1, high)
  elif target < arr[mid]:
    binary_search_recursive(arr, target,low,mid-1)
  else:
    return -1


list = [2,5,6,7,8,9,10,15,20,25,27,29,30,34,36,37,40]
print(binary_search_recursive(list, 29, 0 , 16))
#print(binary_search(list, 29))