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
# def quick_sort(arr, low=None, high=None):
#     if len(arr) <= 1:
#         return arr
#     elif len(arr) == 2:
#         if arr[0] > arr[1]:
#             arr.insert(0, arr.pop())
#         return arr
#     for i in arr:
#         if i < arr[0] and low is None:
#             low = []
#             low.append(i)
#         elif i > arr[0] and high is None:
#             high = []
#             high.append(i)
#     return quick_sort(low) + [arr[0]] + quick_sort(high)

# arr = [20, 2, 1, 89, 43, 67]
# print(quick_sort(arr))

def quick_sort(arr):
    low = []
    high = []
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr.insert(0, arr.pop())
        return arr
    for i in arr:
        if i < arr[0]:
            low.append(i)
        elif i > arr[0]:
            high.append(i)
    return quick_sort(low) + [arr[0]] + quick_sort(high)

arr = [20, 2, 1, 89, 43, 67]
print(quick_sort(arr))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
