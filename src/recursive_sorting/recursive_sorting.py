# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )

    # TO-DO
    a = 0
    b = 0
    minLen = min(len(arrA), len(arrB))
    merged_arr = [0] * (minLen*2 - 1)

    longerArr: list
    if len(arrA) > len(arrB):
        longerArr = arrA
    else:
        longerArr = arrB

    print(minLen)
    for i in range(0, (minLen*2)-1):
        if arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    merged_arr += longerArr[(minLen)-1:]
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
def timsort( arr ):

    return arr
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]

print(merge(arr1, arr4))