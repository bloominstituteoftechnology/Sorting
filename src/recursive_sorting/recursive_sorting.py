# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO
    idx_a, idx_b = 0, 0
    for i in range(elements):
        # if either array is empty, return the other
        if len(arrA) == idx_a:
            for j in range(idx_b, len(arrB)):
                merged_arr[i + j - idx_b] = arrB[j]
            return merged_arr
        elif len(arrB) == idx_b:
            for j in range(idx_a, len(arrA)):
                merged_arr[i + j - idx_a] = arrA[j]
            return merged_arr
        # add element in the right order
        if arrA[idx_a] < arrB[idx_b]:
            merged_arr[i] = arrA[idx_a]
            idx_a += 1
        else:
            merged_arr[i] = arrB[idx_b]
            idx_b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2: # base case
        return arr
    else:
        half = len(arr) // 2
        # print(half)
        left =  arr[:half]
        # print(left)
        right = arr[half:]
        # print(right)

    return merge(merge_sort(left), merge_sort(right))


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
