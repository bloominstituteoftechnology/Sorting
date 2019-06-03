# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1

  # TO-DO: add missing code
  
    while True:
        midpoint = int(high/2)
        if arr[midpoint] == target:
            return midpoint
        if len(arr) == 1 and arr[0] != target:
            return -1
        elif target < arr[midpoint]:
            high = midpoint
            arr = arr[low:midpoint]
        else:
            low = midpoint
            arr = arr[low:high]

binary_search([0,1,2,3,4,5,6,7], 1)


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low+high)//2

    if len(arr) == 0:
      return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

    if arr[middle] == target:
        print("Here is the target:")
        print(target)
        print("Here it is: ")
        print(middle)
        return middle
    elif target < arr[middle]:
        high = middle - 1
        binary_search_recursive(arr, target, low, high)
    else:
        low = middle + 1
        binary_search_recursive(arr, target, low, high)

binary_search_recursive([-11,-8,0,1,2,3,4,5,6,7,8], -8, 0, 8)
