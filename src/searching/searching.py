def linear_search(arr, target):
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i

	return -1   # not found

def binary_search(arr, target):

	if len(arr) == 0:
		return -1 # array empty

	low = 0
	high = len(arr)-1

	while low <= high:
		middle = (low + high) // 2
		if target < arr[middle]:
			high = middle - 1
		elif target > arr[middle]:
			low = middle + 1
		else:
			return middle

	return -1 # not found

def binary_search_recursive(arr, target, low, high):

	middle = (low+high)//2

	if len(arr) == 0:
		return -1 # array empty
	# TO-DO: add missing if/else statements, recursive calls
	if arr[middle] == target:
		return middle
	elif arr[middle] > target:
		return binary_search_recursive(arr, target, low, middle - 1)
	else:
		return binary_search_recursive(arr, target, middle + 1, high)
