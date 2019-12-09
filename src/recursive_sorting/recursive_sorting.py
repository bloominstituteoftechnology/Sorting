# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        split_index = len(arr)//2
        first_half = arr[:split_index]
        second_half = arr[split_index:]
        merge_sort(first_half)
        merge_sort(second_half)
    return arr


nums = [1, 2, 3, 4, 5]
split_index = len(nums)//2
print(nums[:split_index], nums[split_index:])


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

print(merge_sort([1, 2, 3, 4, 5]))