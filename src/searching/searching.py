# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for index in range(0, len(arr)):
        if arr[index] == target:
            return index
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    low = 0
    high = len(arr)-1
    # TO-DO: add missing code
    while low <= high:
        middle_index = (low + high) // 2
        print(f'Middle Index: {middle_index}')
        if target == arr[middle_index]:
            return middle_index
        elif target > arr[middle_index]:
            low = middle_index + 1
        elif target < arr[middle_index]:
            high = middle_index - 1
        else:
            return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
  middle = (low + high)//2
  if len(arr) == 0:
    return -1  # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] == target:
    print(middle)
    return middle
  elif arr[middle] > target:
    high = middle - 1
    return binary_search_recursive(arr, target, low, high)
  elif arr[middle] < target:
    low = middle + 1
    return binary_search_recursive(arr, target, low, high)
  return -1


# print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -9))
array = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(array, -9, 0, len(array)-1))