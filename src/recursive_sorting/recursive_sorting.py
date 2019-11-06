# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        ind = len(arr) // 2
        arrA = merge_sort(arr[:ind])
        arrB = merge_sort(arr[ind:])
        arr = merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    arrA = arr[start:mid]
    arrB = arr[mid:end]
    i = 0
    j = 0
    k = start
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            arr[k] = arrA[i]
            i += 1
        else:
            arr[k] = arrB[j]
            j += 1
        k += 1
    while i < len(arrA):
        arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        arr[k] = arrB[j]
        j += 1
        k += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    if 1 + r - l > 1:
        mid = (1 + r - l) // 2 + l - 1
        arr = merge_sort_in_place(arr, l, mid)
        arr = merge_sort_in_place(arr, mid+1, r)
        arr = merge_in_place(arr, l, mid+1, r+1)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    
    return arr
