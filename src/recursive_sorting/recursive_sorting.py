# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    iM, iA, iB = 0, 0, 0
    while iA < len( arrA ) and iB < len( arrB ):
        if arrA[iA] < arrB[iB]:
            merged_arr[iM] = arrA[iA]
            iA += 1
            iM += 1
        else:
            merged_arr[iM] = arrB[iB]
            iB += 1
            iM += 1

    if iA == len( arrA ):
        merged_arr[iM:] = arrB[iB:]
    else:
        merged_arr[iM:] = arrA[iA:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if arr == []:
        return []

    if not isinstance(arr[0], list):
        arr = list(map(lambda x: [x], arr))

    if len(arr) == 1:
        return arr[0]

    if len(arr) % 2 == 0:
        split1 = arr[:len(arr)//2]
        split2 = arr[len(arr)//2:]
        rem = []
    else:
        split1 = arr[:len(arr)//2]
        split2 = arr[len(arr)//2:-1]
        rem = [arr[-1]]

    merged = [ merge(a, b) for a, b in zip(split1, split2) ] + rem

    return merge_sort(merged)


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
