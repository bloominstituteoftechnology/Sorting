# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    ai = 0
    bi = 0
    if arrA[ai] < arrB[bi]:
        merged_arr[0] = arrA[ai]
        merged_arr[1] = arrB[bi]
        ai += 1
        print(merged_arr)
    else:
        merged_arr[0] = arrB[bi]
        merged_arr[1] = arrB[ai]
        bi += 1
        print(merged_arr)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    arrlen = len(arr)
    if arrlen > 1:
        arr1 = merge_sort(arr[:arrlen // 2])
        arr2 = merge_sort(arr[arrlen // 2:])

        print(arr1)
        print(arr2)
        arr = merge(arr1, arr2)
    
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
