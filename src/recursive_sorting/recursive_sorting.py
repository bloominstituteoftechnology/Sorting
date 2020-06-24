# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    indexA = 0
    indexB = 0
    for i, v in enumerate(merged_arr):
        if indexA >= len(arrA):
            merged_arr[i] = arrB[indexB]
            indexB += 1
        elif indexB >= len(arrB):
            merged_arr[i] = arrA[indexA]
            indexA += 1
        elif arrA[indexA] <= arrB[indexB]:
            merged_arr[i] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[i] = arrB[indexB]
            indexB += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        midIndex = int(len(arr) / 2)
        left = merge_sort(arr[0:midIndex])
        right = merge_sort(arr[midIndex:])
        return merge(left, right)


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
