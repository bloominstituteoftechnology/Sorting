# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    A = 0
    B = 0

    for x in range(0, elements):
      if A >= len(arrA):
        merged_arr[x] = arrB[B]
        B += 1
      elif B >= len(arrB):
        merged_arr[x] = arrA[A]
        A += 1
      elif arrA[A] < arrB[B]:
        merged_arr[x] = arrA[A]
        A += 1
      else:
        merged_arr[x] = arrB[B]
        B += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

  result1 = merge_sort(left)
  result2 = merge_sort(right)

  return merge(result1, result2)

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
