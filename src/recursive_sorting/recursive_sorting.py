# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = j = 0
    index = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[index] = arrA[i]
            i += 1
        else:
            merged_arr[index] = arrB[j]
            j += 1

        index += 1
    while i < len(arrA):
        merged_arr[index] = arrA[i]
        i += 1
        index += 1
    while j < len(arrB):
        merged_arr[index] = arrB[j]
        j += 1
        index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

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


print(merge([1, 3, 5, 8], [2, 3, 7, 9]))
