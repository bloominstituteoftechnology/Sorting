# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) / 2])
        right = merge_sort(arr[len(arr) / 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below
def quick_sort(arr, low, high):
    # if empty arr return empty arr
    if not arr:
        return []
    # End if low index greater or equal to high index of array
    if low >= high:
        return

    pivot = partition(arr, low, high)  # return index of pivot
    quick_sort(arr, low, pivot - 1)  # quicksort left
    quick_sort(arr, pivot + 1, high)  # quicksort right
    return arr


def partition(arr, low, high):
    left = low+1  # initially set to left most index
    right = high  # initially set to right most index
    pivot_value = arr[low]  # pivot is first index

# while left index less than or equal to right index
# loop iterates from left to right
    while left <= right:
        # while value of left value less than pivot and left most index than right index
        while arr[left] < pivot_value and left < right:
            # increment left index until it finds a number greater than pivot value
            left += 1
        # while right index value is greater than pivot value
        while arr[right] > pivot_value:
            # decrement right index until it finds a number less than pivot value
            right -= 1
        # if left index is less than right index
        if left < right:
            # swap left and right values and increment left index and decrement right index
            # This sorts the values on either side of the pivot
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            # if left index is equal to or greater than right index this increments left index.
            left += 1
    # once loop finishes sorting numbers on either side of pivot
    # right = index of pivot
    # This places pivot into correct index spot
    arr[low], arr[right] = arr[right], arr[low]
    # Returns pivot index
    return right

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(quick_sort(arr1, 0, len(arr1)-1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
