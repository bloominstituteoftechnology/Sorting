# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in merged_arr:
        print(arrA,arrB)
        print(arrA[0],arrB[0])
        print(merged_arr)
        print(i)
        i = min(arrA[0], arrB[0])
        print(i, merged_arr)
        if merged_arr == arrA:
            arrA = arrA[1:]
        else:
            arrB = arrB[1:]
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1:
        return arr;
    x = arr[0:len(arr)//2]
    y = arr[len(arr)//2:len(arr)]
    # print(x,y)
    merge(y,x)

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



merge_sort([1,2,3,4,5,6,7,8,9])