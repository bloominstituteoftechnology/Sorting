### helper function
def merge( arrA, arrB ): # left/right as written in merge_sort() below
    elements = len( arrA ) + len( arrB ) # an integer
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
        # split the list down to arrays of one.
    if len( arr ) > 1: # if theres more than one thing, keep:

        # SPLIT from index 0, splice to the midpoint of array. 
        #  `//` returns the math.floor
        # recursive will sort all the the left first (because we told it to)
        # then come back up and do the right, until all are sorted
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )

        # SPLIT from the midpoint to the end
        right = merge_sort( arr[ len( arr ) // 2 : ] )

        arr = merge( left, right )   # merge() helper defined later/seperately
    return arr

# recursive merge sort without helper
def mergeSort(arr):
    print('mergesort call')
    print(arr)

    if len(arr) > 1:
        middle = (len(arr))//2
        L = arr[:middle]
        R = arr[middle:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # merging
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # checking if any element was left out
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(arr)
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(arr)

    return arr

# try it out
print("Merge Sort 2")
arr = [2,5,9,7,4,1,3,8,6];
print(mergeSort(arr))
print(arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
# QUICKSORT ALGORITHM EXPLAINED in C++ 
# (good explanation; uses partition helper): 
# [(https://www.youtube.com/watch?v=7h1s2SojIRw&t=427)]

# a SORTED POSITION is when all the other elements on the left-hand side
# are smaller than the SORTED POSITION and the elements on the right-hand
# side are equal-to or greater than the SORTED POSITION.

def quick_sort(arr, low, high):
    pivot = high
    count = low

    if low < high:
        # ci = current index
        for ci in range(low, high):
            if arr[ci] < arr[pivot]:
                
                #swap positions
                arr[ci], arr[count] = arr[count], arr[ci]
                count += 1

        # RECURSION
        # swap positions
        arr[pivot], arr[count] = arr[count], arr[pivot]
        quick_sort(arr, count + 1, high)
        quick_sort(arr, low, count - 1)

    return arr

print(f"Quick Sort")
array = [4, 2, 3, 1, 6, 5]
print(array)
array = quick_sort(array, 0, len(array) -1)
print(array)

array = [6, 5, 4, 3, 2, 1]
print(array)
array = quick_sort(array, 0, len(array) -1)
print(array)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


 