# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  while len(arr) == 0:
    return -1
  
  low = 0
  high = len(arr) - 1
  while low <= high:
    middle = (low+high) // 2
    print("TARGET>>>>", target)
    print("LOW>>>>", low)
    print("MIDDLE>>>>", middle)
    print("HIGH>>>>>", high)
    if target < arr[middle]:
      high = middle - 1
    elif target > arr[middle]:
      low = middle + 1
    else:
      return middle

  return -1

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  while len(arr) == 0:
    return -1

  middle = (low+high)//2

#check if target is in middle, if so return true
#then check if middle is higher or lower than target
#if target is lower than middle, then middle is new high asdf