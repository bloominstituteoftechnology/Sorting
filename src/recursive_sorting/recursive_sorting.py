# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 40, 60, 600, 10000]
arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def merge(arrA, arrB):
    # print(f"ArrayA: {arrA}")
    # print(f"ArrayB: {arrB}")
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # create variables for the indexes of arrA, arrB, and merged_arr
    # k is the index of the merged_arr that we will be adding a value to, i is the current index we are examining in arrA, and j is the current index in arrB
    i = 0
    j = 0
    k = 0
    # loop while either i or j is smaller than arrA or arrB
    while i < len(arrA) and j < len(arrB):
        # check if the item in arrA is smaller than the item in arrB
        if arrA[i] < arrB[j]:
            # if it is then we set merged_arr[k] to it and increment k and i
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            # otherwise we set it to arrB[j] and increment k and j
            merged_arr[k] = arrB[j]
            k += 1
            j += 1

    # both of these while statements are for if all of either arrA or arrB are empty while the other isn't
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    # print(f"merged array: {merged_arr}")
    return merged_arr


# print(merge(arr1, arr2))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # only run the sort if the array is larger than 1 item
    if len(arr) > 1:
        # find the middle of the array
        middle = len(arr) // 2
        # set up recursion for the two halves of the array that we have split by passing each half into merge_sort; this will eventually result in arrays with only 1 index that will then be joined back together in the correct order
        left_half = merge_sort(arr[:middle])
        right_half = merge_sort(arr[middle:])
        # return the merged array after passing in the left and right halves
        return merge(left_half, right_half)
    else:
        return arr


print(merge_sort(arr3))
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
