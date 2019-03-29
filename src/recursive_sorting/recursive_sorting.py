import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    for i in range(0,elements):
        if(len(arrA)==0 and len(arrB)==0):
            break
        elif(len(arrA)==0):
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif(len(arrB)==0):
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            if(arrA[0] < arrB[0]):
                merged_arr.append(arrA[0])
                arrA.pop(0)
            else:
                merged_arr.append(arrB[0])
                arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr)>1):
        midIndex = math.floor(len(arr)/2)
        arr = merge(merge_sort(arr[0:midIndex]),merge_sort(arr[midIndex:len(arr)]))
    else:
        return arr
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
