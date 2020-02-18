def linear_search(arr, target):
    for it in arr:
        if it == target:
            return arr.index(it)
    return -1  # not found


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    low = 0
    high = len(arr) - 1
    while True:
        midpoint = (low + high) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            low = midpoint
        else:
            high = midpoint


def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2
    print(arr,target,low,high)
    if len(arr) == 0:
        return -1  # array empty
    elif arr[middle]==target:
        return middle
    elif arr[middle]<target:
        binary_search_recursive(arr,target,middle,high)
    else:
        binary_search_recursive(arr,target,low,middle)

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(arr1, -8, 0, len(arr1) - 1))