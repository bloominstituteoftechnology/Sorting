# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            del arrA[0]
        else:
            merged_arr.append(arrB[0])
            del arrB[0]

    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        del arrA[0]
        
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        del arrB[0]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
 arrA = []
    arrB = []
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        arrA = merge_sort(arr[:len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2:])
    
    return merge(arrA, arrB)


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
