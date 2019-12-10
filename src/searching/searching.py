#STRETCH: implement Linear Search				
def linear_search(arr, target):
  index_length = len(arr)
  for i in range(0, index_length):
    if arr[i] == target:
      return i
  return -1   # not found
print(linear_search([5,2,1,8,6,9], 8))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
	first = 0
	last = len(arr)-1
	found = False
	while( first<=last and not found):
		middle = (first + last)//2
		if arr[middle] == target :
			found = True
		else:
			if target < arr[middle]:
				last = middle - 1
			else:
				first = middle + 1
	return found
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
