### helper function
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
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr ):
    # base case, if the array is less than 2 elements we will stop
    if len(arr) < 2:
        return arr
    else:
        # our pivot is the first item in the array
        pivot = arr[0]
        # if our item is less than or equal to our pivot we will put it before the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # if our item is greater than our pivot, we will put it behind the pivot
        greater = [i for i in arr[1:] if i > pivot]
        # recursivley will call quick_sort with less and greater until all items are sorted
        return quick_sort(less) + [pivot] + quick_sort(greater)


    return arr

arr = [2,5,9,7,4,1,3,8,6]
print(arr)
arr = quick_sort( arr )
print(arr)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
