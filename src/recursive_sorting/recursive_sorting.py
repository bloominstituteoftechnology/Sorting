# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elem = len( arrA ) + len( arrB )
    merged_arr = [0] * elem
    # TO-DO
    while ((len(arrA) > 0) | (len(arrB) > 0)):
        if not arrA:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif not arrB:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elif (arrA[0] < arrB[0]):
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elif (arrB[0] < arrA[0]):
            merged_arr.append(arrB[0])
            arrB.pop(0)
        merged_arr.pop(0)
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[0:mid]
        right = arr[mid: ]
        arr = merge(merge_sort(left), merge_sort(right))
    
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
