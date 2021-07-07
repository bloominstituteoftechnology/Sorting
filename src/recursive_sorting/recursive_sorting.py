# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    x = 0
    y = 0
    index = 0
    #sort main array
    while x < len(arrA) and y < len(arrB):
       if arrA[x] < arrB[y]:
          merged_arr[index] = arrA[x]
          x += 1
       else:
          merged_arr[index] = arrB[y]
          y += 1
       index += 1
    #sort remaining arrA values
    while x < len(arrA):
       merged_arr[index] = arrA[x]
       x += 1
       index += 1
    #sort remaining arrB values
    while y < len(arrB):
       merged_arr[index] = arrB[y]
       y += 1
       index += 1
    return merged_arr

print(merge([1,2,3,4],[5,6,7,8]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
       middle = len(arr)/2
       left = arr[:int(middle)]
       right = arr[int(middle):]

       merge_sort(left)
       merge_sort(right)

       x = 0
       y = 0
       index = 0

       while x < len(left) and y < len(right):
          if left[x] < right[y]:
             arr[index] = left[x]
             x += 1
          else:
             arr[index] = right[y]
             y += 1
          index += 1

       while x < len(left):
          arr[index] = left[x]
          x += 1
          index += 1

       while y < len(right):
          arr[index] = right[y]
          y += 1
          index += 1

    return arr

print(merge_sort([54,26,93,17,77,31,44,55,20]))

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
