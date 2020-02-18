

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


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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
