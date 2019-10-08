# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
# helps us to know  number of elements 
# merged_array =[0,0,0,0,0] , it will mean that array Amhas 3 elements and array B has 2  elements 
    # TO-DO
    newArray = []
    while len(arrA) > 0 and len(arrB) > 0:
        if(arrA[0]> arrB[0]):
            newArray.append(arrB[0])
            arrB.remove(arrB[0])
        else:
            newArray.append(arrA[0])
            arrA.remove(arrA(0))
    while len(arrA)> 0:
        newArray.append(arrA[0])
        arrA.remove(arrA[0])
    while len(arrB)>0:
        newArray.append(arrB[0])
        arrB.remove(arrB(0))
    return newArray
    # return newArray


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    print(len(arr))
    if (len(arr) == 1):
        return arr[0]
    else:
        n = int(len(arr)/2)
        arr1 = arr[0:n ]
        arr2 = arr[n+1: len(arr)]

        # TO-DO
    # this recursively divides each array into half
        return merge(merge_sort(arr1), merge_sort(arr2))


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
