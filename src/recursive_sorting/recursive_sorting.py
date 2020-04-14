# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    leftIdx = 0
    rightIdx = 0

    # TO-DO
    while(leftIdx < len(arrA) and rightIdx < len(arrB)):
        if(arrB[rightIdx] > arrA[leftIdx]):
            merged_arr.append(arrA[leftIdx])
            leftIdx += 1
        else:
            merged_arr.append(arrB[rightIdx])
            rightIdx += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    

    half = len(arr) // 2
    arrA = arr[:half]
    arrB = arr[half:]



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
