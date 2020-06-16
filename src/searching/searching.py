# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    if(arr[i]==target):
      return i
  
  # TO-DO: add missing code

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
# The goal of the Binary is to look to an order sequence and determine a value that we looking for
# is in that sequence or not. Example : [1, 3, 4, 6, 7, 8, 9] the number we are looking for is 7.
# The way we are doing is to find the mindpoint and comparing with the number we are looking for.
# If is it higher we choose the items to right or if it is lower we choose the items to the left
# if we find the number we are searching , we stop the algorithm and return the position to the item

def binary_search(arr, target):
  left = 0 # we start with the first element 
  right = len(arr)-1 # and we finish with the last element

  while left <= right:
    midpoint = left + (right - left) // 2 # we want the midpoint here so we put 2
    midpoint_value = arr[midpoint]
    if midpoint_value == target: # if we found the target equal to the midpoint return as back the position
      return midpoint
    elif target < midpoint_value: # the target we are looking for will be at the left
      right = midpoint -1 # the position will be directly to the left of the midpoint
    else:
      left = midpoint + 1 # if the target is greater then we need to check if it is at the right and repositioning
  
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
# we having an index of 5 numbers: [4,7,8,12,45,99] and we set 4 the low number and 99 the high number
# we need to determine a middle index in these array of numbers.
# to do so we say middle = (Lower + Upper) devided by 2: 0 + 5 /2 = 2 (0=4, 5=99)
# searching for 45: we count the index array until the number 45 and devided by 2. The middle is 8
# checking to see if our middle number is the number we are searching it
# if the search value is bigger than the one we searching then middle number becomes new low abd the list came out smaller
# so the new list will be [8, 12, 45, 99] same calculations again and the new list will be [12, 45, 99]

def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  # if value is smaller than the middle , the it can only be in the left index
  if arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle-1)
  elif arr[middle]<target:
    return binary_search_recursive(arr, target, middle+1,high)
  else:
    return middle
