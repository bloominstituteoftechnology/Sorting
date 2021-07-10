# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in arr:
    if i == target:
      return target
    else:
      return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
# works only on a sorted set of elements.
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  def find_middle(arr): 
    low = 0
    high = len(arr)

    # TO-DO: add missing code
    middle = (low + high)//2
    return middle

  temp_middle = find_middle(temparr)
  temp_middle_value == temparr[temp_middle]
  if temp_middle_value == target:
      return target
  else:
    if temp_middle_value < target:
      temparr = arr[:middle]
    elif temp_middle_value > target:
      temparr = arr[middle:]
    else:
      return -1 # not found

# middle = len(arr) / 2 = 20 / 2 = 10
# arr[10] = 15? # nope, check if greater than or less than
# arr[10] > 15? # nope, eliminate LHS of array, continue searching RHS
# middle = len(arr[11: ]) / 2 = 9 / 2 = 4 .  # integer division
# arr[11 + 4] = 15? # yes! we can return the index where the target value can be found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
