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

def create_array(size = 10, max = 50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# test = create_array()
# print(test)
# result = merge_sort(test)
# print(result)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):


    return arr

def merge_sort_in_place(arr, l, r): 


    return arr


# TO-DO: implement the Quick Sort function below
def partition(arr, low, high):
    i = (low - 1) # index of smaller element
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return(i + 1)


def quick_sort( arr, low, high ):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr

test2 = create_array()
print(f'quick_sort before: {test2}')
result2 = quick_sort(test2, 0, len(test2) - 1)
print(f'quick_sort after: {result2}')


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort_in_place(arr1, 0, len(arr1)-1) # [0,1,2,3,4,5,6,7,8,9]
