# TO-DO: complete the helpe function below to merge 2 sorted arrays

"""
need to compare the numbers and sort the elements one by one start with left first index and compare to first right index, if left is smaller put into array and them compare second element to right first and if right is small push to new array and then compare left second element to second right element.
"""


def merge(arrA, arrB):
    merged_arr = []

    # TODO
    i = 0
    j = 0

    while (i < len(arrA) and j < len(arrB)):
        if(arrA[i] < arrB[j]):
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    while (i < len(arrA)):
        merged_arr.append(arrA[i])
        i += 1
    while (j < len(arrB)):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

"""
merge takes two sorted arrays and merges them together.
I need to keep calling merge sort until the array is divided
into arrays of 1, so they are technically sorted and then
call merge on them to merge them.
"""


def merge_sort(arr):
    # TO-DO
    middle = len(arr) // 2

    # split the arrays down the middle
    arrA = arr[:middle]
    arrB = arr[middle:]

    """
    base case for recursion function, so it returns when the arr
    is only has one value.
    """
    if len(arr) <= 1:
        return arr

    """
    executing the recursive function that will keep dividing
    the arrays until they only have one value and are "sorted".
    once it hits the base case it will start executing merge on
    the returning functions.
    """
    return merge(merge_sort(arrA), merge_sort(arrB))

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
