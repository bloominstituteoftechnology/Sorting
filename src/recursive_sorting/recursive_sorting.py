# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    arrC = []
    # TO-DO
    while len( arrA ) > 0 and len( arrB ) > 0:
      if arrA[0] > arrB[0]:
        arrC.append(arrB[0])
        arrB.remove(arrB[0])
      else:
        arrC.append(arrA[0])
        arrA.remove(arrA[0])
    while len(arrA) > 0:
      arrC.append(arrA[0])
      arrA.remove(arrA[0])

    while len(arrB) > 0:
      arrC.append(arrB[0])
      arrB.remove(arrB[0])
    
    return arrC


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1:
      return arr

    arr1 = arr[len(arr) // 2:]
    arr2 = arr[:len(arr) // 2]
    
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)



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
