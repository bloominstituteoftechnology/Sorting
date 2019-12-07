# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO 
    print(elements)
    # counter for lengths of all 3 arrays
    i, j, k = 0,0,0

    while i < len(arrA) and j < len(arrB):
      if arrA[i] < arrB[i]:
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
      else:
        merged_arr[k] = arrB[j]
        j+= 1
        k +=1

    while i < len(arrA):
      merged_arr[k]  = arrA[i]
      i +=1
      k +=1
    
    while j < len(arrB):
      merged_arr[k] = arrB[j]
      k +=1
      j +=1
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
    arr = []
    arr.append(merge(left, right))
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
