

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    print(f"Middle: {middle}")
    first_half = []
    second_half = []
    print(arr[middle])
    for i in range(0, middle):
        first_half.append(arr[i])
        print(first_half)
    for i in range(middle, len(arr)):
        second_half.append(arr[i])
        print(second_half)
    merge_sort(first_half)
    merge_sort(second_half)
          

    return arr

merge_sort([2, 9, 4, 16, 3, 7, 10])
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
