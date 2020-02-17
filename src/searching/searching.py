# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, n):
	low = 0
	high = len(arr) -1
	while high > low:
		middle = (low + high) // 2
		if arr[middle] == n:
			return middle
		elif arr[middle] > n:
			high = middle
		elif arr[middle] < n:
			low = middle
	return -1


def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0:
      return -1

    middle = (low + high)//2

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, 0, middle)
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle, len(arr) - 1)