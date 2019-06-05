# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    if arrA > arrB:
        merged_arr[len(arrA):] = arrA
        merged_arr[:len(arrB)] = arrB
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2: # base case
        return arr
    else:
        half = len(arr) // 2
        # print(half)
        left = [el for el in arr[:half]]
        # print(left)
        right = [el for el in arr[half:]]
        # print(right)

    return merge_sort(left), merge_sort(right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
