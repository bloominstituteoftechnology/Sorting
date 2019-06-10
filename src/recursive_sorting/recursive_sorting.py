def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a, b, m = 0, 0, 0

    # Loop through arrays, adding smallest element from each to merged array
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a] # Add a to merged
            a += 1 # Increment a
        else: # Else also handles a = b
            merged_arr[m] = arrB[b] # Add b to merged
            b += 1 # Increment b
        m += 1 # Increment m

    # Might have some leftovers... Previous loop ends when one reaches the end
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1

    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) > 1:
        mid = len(arr) // 2
        arrA = merge_sort(arr[:mid]) # Sort left
        arrB = merge_sort(arr[mid:]) # Sort right
        arr = merge(arrA, arrB)

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
def timsort( arr ):

    return arr
