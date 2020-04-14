# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0

    return merged_arr

# EXAMPLE:
def merge( arrA, arrB ):
    # TO-DO
    i=0
    j=0
    lenA = len(arrA)
    lenB = len(arrB)

    arr = []

    while((i < lenA) and (j < lenB)):
        if(arrA[i] < arrB[j]):
            arr.append(arrA[i])
            i = i + 1
        else:
            arr.append(arrB[j])
            j = j + 1
    
    while(i < lenA):
        arr.append(arrA[i])
        i = i + 1
    
    while(j < lenB):
        arr.append(arrB[j])
        j = j + 1
    
    return merged_arr
                   
arrA = [1, 4, 7, 9]
arrB = [10, 14, 15]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    def merge_sort( arr ):
    if len(arr) > 1:
        # split the array
        mid = len(arr) // 2
        # split again - left
        left = arr[:mid]
        # split again - right
        right = arr[mid:]
        arr = merge(left, right)

        mergeSort(left)
        mergeSort(right)

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
