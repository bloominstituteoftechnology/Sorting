### helper function
from random import randint

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        middleindex = int(len( arr ) / 2)
        left = merge_sort( arr[ 0 : middleindex ] )
        right = merge_sort( arr[middleindex: ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below
def quick_sort( arr, low, high ):  
  if len(arr) < 2:
    return arr
  else:
    pivot = randint(0,len(arr)-1)
    left = []
    right = []
    for n in arr:
      if n < arr[pivot]:
        left.append(n)
      if n > arr[pivot]:
        right.append(n)
  return quick_sort(left, 0, len(left)-1) +  [arr[pivot]] + quick_sort(right, 0,len(right)-1)
 

# def quick_sort(arr,low,high):
#   if len(range(low,high)) < 2:
#     return arr[low:high]

#   pivot = randint(0,len(arr))

#   for n in arr:
#     if n < arr[pivot]:


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr