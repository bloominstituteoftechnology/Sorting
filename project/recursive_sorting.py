from iterative_sorting import insertion_sort

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
        arr = merge( left, right )   # merge() defined earlier
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


def quick_sort(arr):

    if len(arr) <= 1: # if list only has 1 item, it's already sorted
        return arr
    if len(arr) == 2: # if list only has 2 items
        if arr[0] > arr[1]: # and the first item is larger than the second
            last = arr.pop() # pop the second item
            arr.insert(0, last) # and insert it into the first position
        return arr

    pivot = arr[0]
    low = []
    high = []
    
    for item in arr[1:]:
        if item < pivot: # if item is lower than the pivot
            low.append(item) # add to low list
        if item > pivot: # if it's higher
            high.append(item) # add to high list
        # currently doesn't handle duplicates

    return quick_sort(low) + [pivot] + quick_sort(high)


arr = [2, 5, 9, 7, 4, 1, 3, 8, 6, 12, 542, 24314, 23]


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr, run=3, merged=[] ):

    if len(arr) == 0:
        return merged
    if len(arr) == 1: # if list only has 1 item, it's already sorted
        return merge(arr, merged) # merge sorted arr and previously merged
    if len(arr) == 2: # if list only has 2 items
        if arr[0] > arr[1]: # and the first item is larger than the second
            last = arr.pop() # pop the second item
            arr.insert(0, last) # and insert it into the first position
        return merge(arr, merged) # return the sorted array
    if len(arr) < run: # if length of list is smaller than the run
        return merge(insertion_sort(arr), merged) # calls insertion_sort on arr and merges with previously merged

    # out of bounds splicing works so if len(arr) < run or run*2 following code still works correctly
    first = insertion_sort(arr[:run]) # sorts first "batch"
    second = insertion_sort(arr[run : run * 2]) # sorts second "batch"
    merged_f_s = merge(first, second) # merges first and second
    return timsort(arr[run * 2 :], merged=merge(merged_f_s, merged)) # recursion 

arr = timsort(arr)
print("THIS IS TIMSORT", arr)