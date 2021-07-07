# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i = i + 1
        else:
            merged_arr.append(arrB[j])
            j = j + 1

    merged_arr = merged_arr + arrA[i:]
    merged_arr = merged_arr + arrB[j:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        mid = int(len(arr) / 2)
        l = merge_sort(arr[:mid])
        r = merge_sort(arr[mid:])
        return merge(l, r)


print(merge_sort([7, 6, 5, 3, 1, 4, 2, 8]))
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
