# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, len(arrA)):
        merged_arr[i] = arrA[i]
        print(merged_arr)
    for j in range(len(arrA), elements):
        merged_arr[j] = arrB[j - len(arrA)]
        print(merged_arr)
    return merged_arr

arrX = [1,2,3]
arrY = [5,6,7,8,9]
merge(arrX, arrY)

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
