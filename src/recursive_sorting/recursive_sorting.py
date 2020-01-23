# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    index_merged = index_A = index_B = 0
    for index_merged in range(elements):
        if index_A == len(arrA):
            merged_arr[index_merged:] = arrB[index_B:]
            break
        elif index_B == len(arrB):
            merged_arr[index_merged:] = arrA[index_A:]
            break
        elif arrA[index_A] <= arrB[index_B]:
            merged_arr[index_merged] = arrA[index_A]
            index_A += 1
        elif arrB[index_B] <= arrA[index_A]:
            merged_arr[index_merged] = arrB[index_B]
            index_B += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        return merge(merge_sort(left_arr), merge_sort(right_arr))
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
def timsort(arr):

    return arr
