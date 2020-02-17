# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]

    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA = arrA[1:]

    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB = arrB[1:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) == 0:
        return arr
    end_idx = len(arr)
    mid_idx = len(arr) // 2
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[0:mid_idx])
    right = merge_sort(arr[mid_idx:end_idx])
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
def timsort(arr):

    return arr
