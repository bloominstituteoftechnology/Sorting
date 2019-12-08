# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    res = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            res.append(arrA.pop(0))
        else:
            res.append(arrB.pop(0))
    if len(arrA) > 0:
        res.extend(arrA)
    else:
        res.extend(arrB)
    return res


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        arrA = merge_sort(arr[:mid])
        arrB = merge_sort(arr[mid:])
        arr = merge(arrA, arrB)
        return arr


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):

    # STRETCH: implement the Timsort function below
    # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


