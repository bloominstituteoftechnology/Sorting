# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    L = 0
    R = 0
    for i in range(0, elements):
        if L >= len(arrA):
            merged_arr[i] = arrB[R]
            R += 1
        elif R >= len(arrB):
            merged_arr[i] = arrA[L]
            L += 1
        elif arrA[L] < arrB[R]:
            merged_arr[i] = arrA[L]
            L += 1
        else:
            merged_arr[i] = arrB[R]
            R += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    
    if(len(arr) <= 1):
        return arr
    else:
        half = len(arr) // 2
        arr1 = arr[half:]
        arr2 = arr[:half]

        ms_1 = merge_sort(arr1)
        ms_2 = merge_sort(arr2)

        return merge(ms_1, ms_2)
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
