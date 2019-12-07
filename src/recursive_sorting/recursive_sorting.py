# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    print(merged_arr)

    return merged_arr


# merge([2, 2, 3], [2, 2, 3])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        # Recursive call on each half to divide them
        merge_sort(left)
        merge_sort(right)
        # print("I am Middle: ", middle)
        # print("I am the Left: ", left)
        # print("I am the right: ", right)
        # print("Printing mergeSort left: ", merge_sort(left))
        # print("Printing mergeSort Right: ", merge_sort(right))

    return arr


merge_sort([3, 7, 1, 5, 4])


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
