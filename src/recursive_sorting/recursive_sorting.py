l = [1, 5, 8, 4, 2, 9, 6, 0, 10, 3, 7]


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    print(f"elements: {elements} - merged_arr {merged_arr}")

    return merged_arr



# x = merge(l[:4], l[4:])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if (len(arr) == 1):
        return arr

    half_len = len(arr)//2

    # get first half
    arr1 = l[:half_len]

    # get second half
    arr2 = l[half_len:]

    print(f"{arr1} - {arr2}")

    return arr



# print(l)
# print(l[:len(l)//2])
# print(l[len(l)//2:])


merge_sort(l)


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
