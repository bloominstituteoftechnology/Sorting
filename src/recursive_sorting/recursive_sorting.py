# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    idx_a, idx_b = 0, 0
    for i in range(elements):

        # Take care of the condition where one of the arrays
        # no longer has any elements in it
        if len(arrA) == idx_a:
            for j in range(idx_b, len(arrB)):
                merged_arr[i + j - idx_b] = arrB[j]
            return merged_arr
        elif len(arrB) == idx_b:
            for j in range(idx_a, len(arrA)):
                merged_arr[i + j - idx_a] = arrA[j]
            return merged_arr

        if arrA[idx_a] < arrB[idx_b]:
            merged_arr[i] = arrA[idx_a]
            idx_a += 1
        else:
            merged_arr[i] = arrB[idx_b]
            idx_b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Only one element, means it's sorted

    split_point = len(arr) // 2
    return merge(merge_sort(arr[:split_point]), merge_sort(arr[split_point:]))


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
