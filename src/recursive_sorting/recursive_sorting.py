# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB, merged_arr ):
    merged_arr = []
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    while len(arrA):
        merged_arr.append(arrA.pop(0))
    while len(arrB):
        merged_arr.append(arrB.pop(0))
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
