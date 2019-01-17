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
        left = merge_sort( arr[ 0 : int(len( arr ) / 2) ] )
        right = merge_sort( arr[ int(len( arr ) / 2) : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start=None, mid=None, end=None):
    # TO-DO
    start = 0
    end = len(arr) - 1
    mid = int((start + end) / 2)
    if arr[mid] > arr[mid+1]:
        arr[mid], arr[mid+1] = arr[mid+1], arr[mid]
    return arr
# print(merge_in_place([6, 2]))


# def merge_sort_in_place(arr, l=None, r=None): 
def merge_sort_in_place(arr):
  

    for i in range(0, len(arr), 2):
        if arr[i] > arr[i+1]:
            [arr[i]], [arr[i + 1]] = [arr[i + 1]], [arr[i]]

        for i in range(0, len(arr)-2, 3):
            if arr[i+1] > arr[i+2]:
                [arr[i+1]], [arr[i + 2]] = [arr[i + 2]], [arr[i+1]]
    print(arr)
    return 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort_in_place(arr1))

# TO-DO: implement the Quick Sort function below
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    if low >= 0:
        print(arr[low], arr[high])
        
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return i + 1
def quick_sort( arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr
length = len(arr1)
print(quick_sort(arr1, 0, length -1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr