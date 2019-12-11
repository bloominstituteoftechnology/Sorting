# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):
        # make sure both arrays aren't empty
        if len(arrA) > 0 and len(arrB) > 0:
            # check first element of each array, see which is smaller
            # if arrA[0] is smaller, add it to merged_arr and delete it from arrA
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0])
            # if arrB[0] is smaller, add it to merged_arr and delete it from arrB
            else:
                merged_arr[i] = arrB[0]
                arrB.remove(arrB[0])
        # if either array is empty:
        else:
            if len(arrA) == 0:
                # if arrA is empty, add the next element from arrB to merged_arr and delete it from arrB
                merged_arr[i] = arrB[0]
                arrB.remove(arrB[0])
            else:
                #  otherwise if arrB is empty, add the next element from arrA and then delete it from arrA
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0])
    print("we have merging:", merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    print("we are splitting:", arr)
    if len(arr) > 1:
        # divide the array and assign both halves
        midpoint = len(arr)//2
        # recursively split each side until there is only one element
        left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])
        # merge the two sides together
        arr = merge(left, right)
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
