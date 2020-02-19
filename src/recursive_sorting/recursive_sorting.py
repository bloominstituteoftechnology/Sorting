# Quick Sort Algorithm
# 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
# 2. Move all elements smaller than the pivot to the left.
# 3. Move all elements greater than the pivot to the right.
# 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
def partition(data):
    left = []
    pivot = data[0]
    right = []
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:  # Handling the > or ==
            right.append(item)
    return left, pivot, right


def quicksort(data):
    if not data:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)


def quicksort_students(arr):
    if arr:
        import random
        pivot = random.choice(arr)
        low = [n for n in arr if n < pivot]
        middle = [n for n in arr if n == pivot]
        high = [n for n in arr if n > pivot]
        return [*quicksort(low), *middle, *quicksort(high)]
    else:
        return []


# Algorithm
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
# Below: A helper function that handles merging sorted pieces back together
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # Since arrA/B are already sorted, prepare first element of each when merging
    for i in range(0, elements):
        if a >= len(arrA):  # All the elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # All the elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # The next element in arrA if smaller add to the final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # The next element in arrB if smaller add to the final array
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# Below: A recursive function that handles dividing the array (or subarray) in half
def merge_sort(arr):
    if len(arr) > 1:
        half = len(arr) // 2
        left = merge_sort(arr[0:half])
        right = merge_sort(arr[half:])
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
