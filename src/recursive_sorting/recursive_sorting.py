# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0 # for left list or arrA
    j = 0 # for right list or arrB
    k = 0 # for tracking the index of the merged_arr
    # if the arrays equal length
    while i < len(arrA) and j < len(arrB):
      if arrA[i] < arrB[j]:
        merged_arr[k] = arrA[i]
        i += 1
      else:
        merged_arr[k]= arrB[j]
        j += 1
      k += 1  
    # if arrB  has fewer elements than arrA
    while i < len(arrA):
      merged_arr[k]= arrA[i]
      i += 1
      k += 1
    # if arrA has fewer elements than arrB
    while j < len(arrB):
      merged_arr[k]=arrB[j]
      j += 1
      k += 1
          
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Base case
    if len(arr)<=1:
      return arr
    #Find the midpoint
    midpoint = len(arr)//2
    # Divide
    left_arr = arr[:midpoint]
    right_arr = arr[midpoint:]
    # Conquer
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    # merge the left and right now
    arr = merge(left,right)
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
