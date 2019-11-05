# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    print(arrA)
    print(f"arrB: {arrB}")

    for i in range(0, elements):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
            elif arrB[0] < arrA[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)
        elif len(arrA) > 0 and len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif len(arrA) == 0 and len(arrB) > 0:
            merged_arr[i] = arrB.pop(0)

    print(f"merged: {merged_arr}")

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    halfway = 0

    if len(arr)%2 != 0:
        halfway = len(arr)/2
    else:
        halfway = (len(arr)-1)/2

    if len(arr) > 1:
        arrA = arr[0:int(halfway)+1]
        arrB = arr[int(halfway)+1:]
        arr = merge(merge_sort(arrA), merge_sort(arrB))

    return arr

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


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
