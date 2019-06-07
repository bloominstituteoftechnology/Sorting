# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    x = 0
    y = 0
    index = 0
    #sort main array
    while x < len(arrA) and y < len(arrB):
       if arrA[x] < arrB[y]:
          merged_arr[index] = arrA[x]
          x += 1
          index += 1
       else:
          merged_arr[index] = arrB[y]
          y += 1
          index += 1
    #sort remaining arrA values
    while x < len(arrA):
       merged_arr[index] = arrA[x]
       x += 1
       index += 1
    #sort remaining arrB values
    while y < len(arrB):
       merged_arr[index] = arrB[y]
       y += 1
       index += 1
    return merged_arr

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge( arr1, arr2 ))
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
