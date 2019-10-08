# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    #counters for lengths of all 3 arrays
    i, j, k = 0, 0, 0

    #traverse both arrays
    while i < len( arrA ) and j < len ( arrB ):

        # check if the current element of A is smaller than current element of B
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1
    #iterate through remaining elements of each array
    while j < len( arrB ):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    
    while i < len( arrA ):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    
    # print(f'i {i}, j {j}, k {k}')
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base case
    if len( arr ) <= 1:
        return arr

    half = len( arr ) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


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

# quick sort

# Polya's
# 1 Understand the problem
# 2 Devise a plan
# 3 Carry out the plan
# 4 Look Back

# def quicksort(items):
#     # 0. base case
#     if len(items)<= 1:
#         return items
    
#     # 1. Select the last element as the pivot
#     pivot = items[-1]
#     left = []
#     right = []

#     for i in range(len(items)-1):
#         item = items[i]

#         if item < pivot:
#             left.append(item)
#         else:
#             right.append(item)
#     return quicksort(left) + [pivot] + quicksort(right)