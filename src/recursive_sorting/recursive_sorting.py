# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # check arrA value 0 against arrB value 0 
    #append smaller value to sorted array

    for i in range(0, len(merged_arr)) :
        if not arrA or arrA[0] > arrB[0]:
            merged_arr[i] = arrB.pop(0)
        elif not arrB or arrB[0] > arrA[0]:
            merged_arr[i] = arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
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
def timsort( arr ):

    return arr
