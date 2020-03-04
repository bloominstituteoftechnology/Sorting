# TO-DO: complete the helpe function below to merge 2 sorted arrays
#TAKES IN 2 ARRAYS AND SETS THE AMOUNT OF ELEMENTS IN THE ARRAY BY TAKING THE LENGTH OR ARRAY 1 TO THE LENGTH OF ARRAY 2
#SET TWO VARIABLES WITH FOR THE NEW ARRAYS
#LOOP THROUGH THE ARRAY AND SORT IT
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
#TAKES IN AN ARRAY
#IF LENGTH OF THE ARRAY IS GREATER THAN 1
#SPLIT THE ARRAY IN HALF / BREAK IT INTO 2 LISTS
#MERGE THE LISTS BACK TOGETHER AND RETURN THE NEW ARRAY

def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0:int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)
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
