# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    c = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a = a + 1
        else:
            merged_arr[c] = arrB[b]
            b = b + 1

        c = c + 1

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        a = a + 1
        c = c + 1

    while b < len(arrB):
        merged_arr[c] = arrB[b]
        b = b + 1
        c = c + 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    if len(arr) > 1:
        leftArr = merge_sort(left)
        rightArr = merge_sort(right)
        arr = merge(leftArr, rightArr)
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
