# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    while (arrA or arrB):
        if not arrB or (arrA and arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort(arr[:int(len( arr ) / 2)]) #fixes error: TypeError: slice indices must be integers or None or have an __index__ method
        right = merge_sort(arr[int(len( arr ) / 2):])
        arr = merge( left, right )   # merge defined above function
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
