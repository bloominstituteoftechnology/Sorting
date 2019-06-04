# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    while arrA and arrB:
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
            i += 1
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]
            i += 1
    while arrA:
        merged_arr[i] = arrA[0]
        del arrA[0]
        i += 1
    while arrB:
        merged_arr[i] = arrB[0]
        del arrB[0]
        i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    arr1 = arr[:n//2]
    arr2 = arr[n//2:]
    return merge(merge_sort(arr1), merge_sort(arr2))


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
