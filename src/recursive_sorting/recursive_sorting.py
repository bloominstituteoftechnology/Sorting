# elif = else if
# range() is a function generates a list
# this is then used to iterate over in 'for' loops


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    y = 0
    x = 0

    for i in range( 0, elements):
        if x >= len(arrA):          #arrA elements merged
            merged_arr[i] = arrB[y]
            y += 1
        elif y >= len(arrB):
            merged_arr[i] = arrA[x] #arrB elements merged
            x += 1
        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x] # if the next element is arrA is smaller, add to final array
            x += 1
        else:
            merged_arr[i] = arrB[y] # if next element is actually smaller in arrB, then add to final array
            y += 1


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
