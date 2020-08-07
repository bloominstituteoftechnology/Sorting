# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arrA_length = len(arrA)
    arrB_length = len(arrB)
    merged_arr = []
    i, j = 0, 0

    while i < arrA_length and j < arrB_length:
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    merged_arr = merged_arr + arrA[i:] + arrB[j:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        middle = int(len(arr)/2)
        Lhs = merge_sort(arr[:middle])
        Rhs = merge_sort(arr[middle:])
        return merge(Lhs, Rhs)


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
