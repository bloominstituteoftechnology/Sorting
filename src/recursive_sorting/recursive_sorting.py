# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0
    print(elements)
    print(merged_arr)

    for n in range(0, elements):
        if a >= len(arrA):
            merged_arr[n] = arrB[b]
            b = b + 1
        elif b >= len(arrB):
            merged_arr[n] = arrA[a]
            a = a + 1            
        elif arrB[b] > arrA[a]:
            merged_arr[n] = arrA[a]
            a = a + 1
            
        else:
            merged_arr = arrB[b]
            b += 1
    print(merged_arr)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if 1 < len(arr):

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
