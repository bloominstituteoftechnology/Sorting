# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # keep looping until we look at everything in both arrays
    while max(len(arrA), len(arrB)) > 0:
        for i in range(len(merged_arr)):  # begin to assign things its place in merged_arr
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            elif len(arrB) == 0:
                merged_arr[i] = arrA.pop(0)
            elif arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:  # arrA[0] > arrB[0]
                merged_arr[i] = arrB.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        # halve the array
        arrA = merge_sort(arr[:len(arr)//2])
        arrB = merge_sort(arr[len(arr)//2:])

        arr = merge(arrA, arrB)
    return arr


my_arr = [2, 11, 9, 7, 3, 4, 3, 8, 6, 1]
print(my_arr)
my_arr = merge_sort(my_arr)
print(my_arr)

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
