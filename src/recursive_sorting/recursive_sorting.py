import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB, arr):
    print(f'run: {arrA}, {arrB}')
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # # TO-DO
    i, j, k = 0, 0, 0  # i= arrA counter, j= arrB counter, k= master counter

       # run until left or right is out
    while i < len(arrA) and j < len(arrB):
        # if current arrA val is < current arrB val; assign to master list
        if arrA[i] < arrB[j]:
            arr[k] = arrA[i]
            i += 1
            k += 1
        # else assign arrB to master
        else:
            arr[k] = arrB[j]
            j += 1
            k += 1

    # handle remaining items in remaining list
    remaining = arrA if i < j else arrB
    r = i if remaining == arrA else j

    while r < len(remaining):
        arr[k] = remaining[r]
        r += 1
        k += 1

    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    result = []
    if len(arr) == 0:
        return result
    elif len(arr) == 1:
        return arr
    else:
        middle = int(len(arr)/2)
        print(f'middle: {middle}')
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        print(f'arr1: {arr1}, arr2: {arr2}')
        result = merge(arr1, arr2, arr)
    return result


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


print(merge_sort([0, 1, 2, 3, 4, 5]))
