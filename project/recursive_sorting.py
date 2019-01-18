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
def quick_sort( arr ):
    if len(arr) == 0:
        return arr

    pivot_index = int( len(arr) / 2 )
    pivot = arr[pivot_index]
    less_than = []
    greater_than = []


    for i in range(len(arr)):
        current_num = arr[i]

        if i == pivot_index:
            pass

        elif i < pivot_index and current_num > pivot:
            greater_than.append(current_num)
        
        elif i < pivot_index and current_num < pivot:
            less_than.append(current_num)
        
        elif i > pivot_index and current_num < pivot:
            less_than.append(current_num)
        
        else:                                           # i > pivot_index and current_num < pivot
            greater_than.append(current_num)

    result = quick_sort(less_than) + [pivot] + quick_sort(greater_than) # pivot must be in a list itself in order to concatenate with other lists

    return result

print(quick_sort([2, 1, 3, 4, 9, 7, 5, 0, -1, 1000]))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr