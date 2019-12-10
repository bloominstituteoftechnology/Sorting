# TO-DO: complete the helpe function below to merge 2 sorted leftys
def merge( left, right ):
    # elements = len(left) + len(right)
    # merged_arr = [0] * elements
    # TO-DO
    left_indx = 0
    right_indx = 0
    merged_arr = []

    # while loop with conditional to iterate over the 2 arrays in args
    while left_indx < len(left) and right_indx < len(right):
#comparing left array iterative to right array iterative    
#                 v                   v
      if left[left_indx] < right[right_indx]:
        merged_arr.append(left[left_indx])
        left_indx += 1
      else:
        merged_arr.append(right[right_indx])
        right_indx += 1

    merged_arr += left[left_indx:]
    merged_arr += right[right_indx:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    import math
    # TO-DO
    if len(arr) <= 1:
      return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)





print(merge_sort([4,6,2,78,2,45,7,890,2,2345,65,23,24,1,22,45,22,44]))
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
