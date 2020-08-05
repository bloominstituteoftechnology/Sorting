# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    j, k = 0, 0
    for i in range(len(merged_arr)):
        if k > len(arrB) - 1:
            merged_arr[i] = arrA[j]
            j += 1
        elif j > len(arrA) - 1:
            merged_arr[i] = arrB[k]
            k += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        elif arrB[k] < arrA[j]:
            merged_arr[i] = arrB[k]
            k += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        arrA = arr[:len(arr) // 2]
        arrB = arr[len(arr) // 2:]
        return merge(merge_sort(arrA), merge_sort(arrB))
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
