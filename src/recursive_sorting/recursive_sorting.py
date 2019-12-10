# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print("A:", arrA, "B:", arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    i = 0
    while (len(arrA) > 0) and (len(arrB) > 0):
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            i += 1
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            i += 1
            del arrB[0]
    if len(arrA) > 0:
        for elem in arrA:
            merged_arr[i] = elem
            i += 1
    elif len(arrB) > 0:
        for elem in arrB:
            merged_arr[i] = elem
            i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        split_index = len(arr)//2
        first_half = arr[:split_index]
        second_half = arr[split_index:]
        arr = merge(merge_sort(first_half), merge_sort(second_half))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
