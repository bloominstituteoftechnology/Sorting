# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    x = 0
    y = 0
    for i in range( 0, elements ):
        if x >= len(arrA):
            merged_arr[i] = arrB[y]
            y += 1
        elif y >= len(arrB):
            merged_arr[i] = arrA[x]
            x += 1
        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len( arr ) > 1:
        first = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        second = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( first, second )
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
