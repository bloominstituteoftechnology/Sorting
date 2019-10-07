# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # iterate through the list once
  # also, the tests seem to want me to return the target index,
  # so that's what you get.

  for i in range(0, len(arr)):

    # check if ith element == target
    if arr[i] == target:
      return i
  
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    
    # test to see if the array is empty
    if len(arr) == 0:
        return -1 # array empty

    # set the start to the 0th element, the end to the last element (-1 to avoid an 
    # index out of bounds error)
    start = 0
    end = len(arr)-1
    
    # this really f***d me up for a while, you have to have while >= 0 or you will miss the 
    # edge case where values are right next to each other

    while end - start >= 0:
        mid = start + (end - start) // 2
        item = arr[mid]
        
        # print(f'item: {item}')
        # print(f'target: {target}')
        # print(f'mid: {mid}')
        # print(f'end: {end}')
        # print(f'start: {start} \n')
        
        
        if item < target:
            start = mid + 1
        elif item > target:
            end = mid -1
        else:
            return mid
            

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  # test to see if the array is empty
  if len(arr) == 0:
      return -1 # array empty

  if (high - low) % 2 == 1:
    middle = (high+1) // 2
  else:
    middle = (low + (high - low)) // 2
  
  item = arr[middle]

  print(f'item: {item}')
  print(f'target: {target}')
  print(f'middle: {middle}')
  print(f'high: {high}')
  print(f'low: {low} \n')

  
  if item == target:
    print(f'return: {middle, type(middle)}')
    return int(middle)

  elif item < target:
    binary_search_recursive(arr, target, middle+1, high )
  
  elif item > target:
    binary_search_recursive(arr, target, low, middle-1)

  else:
    return -1
  
  