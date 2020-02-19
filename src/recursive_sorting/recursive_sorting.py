# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []

    # TO-DO
    a = 0
    b = 0 
    for i in range (0, elements): 
        # we are done with arrA:
        if a >= len(arrA):
            merged_arr.append(arrB[b])
            b = b + 1
        # we are done with arrB:
        elif b >= len(arrB):
            merged_arr.append(arrA[a])
            a = a + 1
        elif  arrA[a] <= arrB[b]: 
            merged_arr.append(arrA[a])
            a = a + 1
        else: 
            merged_arr.append(arrB[b])
            b = b + 1 
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        a = merge_sort(arr[0:mid])
        b = merge_sort(arr[mid:])
        arr = merge(a, b)
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
