### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the low element of each when merging!
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
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
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
     if low < high: 
        pi = partition(arr,low,high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot =arr[low]
    left_wall=low

    for i in range (low+1,high):
        if arr[i]<pivot:
            arr[i],arr[left_wall] = arr[left_wall],arr[i] 
            left_wall = left_wall + 1
    pivot,arr[left_wall] = arr[left_wall],pivot

    return left_wall
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
quick_sort(arr1, 0, len(arr1)-1)
print(arr1)




# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr