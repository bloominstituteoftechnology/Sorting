# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len(arr) <= 1:
        return arr
    # TO-DO
    half = len( arr ) // 2

    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    arr =[]

    while left and right:
      if left[0] < right[0]:
        arr.append(left.pop(0))
      else:
        arr.append(right.pop(0))
    
    while left:
      arr.append(left.pop(0))
    while right:
      arr.append(right.pop(0))

    return( arr)


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
