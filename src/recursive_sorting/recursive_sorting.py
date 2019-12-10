# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    print(merged_arr)
    print(arrA, arrB)
    
    if arrA < arrB:

      print("SMOL")

    return merged_arr


"""
3 cases
[5] [3, 8]
[7] [1]
[6] [7, 1]

[5] [3,8]

"""

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len( arr ) > 1:
      m = len(arr) / 2
      l = merge_sort(arr[:int(m)])
      r = merge_sort(arr[int(m):])
      merge(l,r)
    return arr

print(merge_sort([5,3,8,6,7,1]))

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
