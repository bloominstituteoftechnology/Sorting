# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1


# STRETCH: write an iterative implementation of Binary Search 
def find_value_binary(arr, value):
    if len(arr) <= 1:
        # TODO Handle edge
        pass

    first = 0
    last = (len(arr) - 1)
    found = False

    while first <= last and not found:
        # find middle using integer divsion
        middle = (first + last) // 2
        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = middle + 1
    return found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
