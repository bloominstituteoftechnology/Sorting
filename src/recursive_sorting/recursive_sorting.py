# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB, merged_arr ):
    ixA = 0
    ixB = 0
    ixm = 0
    while ixm < len(merged_arr):
        if ixA == len(arrA):
            merged_arr[ixm] = arrB[ixB]
            ixB += 1
        elif ixB == len(arrB):
            merged_arr[ixm] = arrA[ixA]
            ixA += 1
        elif arrA[ixA] < arrB[ixB]:
            merged_arr[ixm] = arrA[ixA]
            ixA += 1
        else:
            merged_arr[ixm] = arrB[ixB]
            ixB += 1
        ixm += 1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    else:
        split = int(len_arr / 2)
        return merge(merge_sort(arr[:split]), merge_sort(arr[split:]), arr)

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
