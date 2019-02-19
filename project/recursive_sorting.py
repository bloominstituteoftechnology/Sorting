import random
myList = [random.randint(0, 10000) for i in range(0, 10000)]

# ### helper function


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
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

# recursive sorting function


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# print(merge_sort(myList))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr):
        # base case (arrays with 0 or 1 are already sorted)
    if (len(arr) < 2):
        # so just return the array
        return arr
    else:
        # else start your pivot at the first number
        pivot = arr[0]
        # sub array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(myList))


# print(quick_sort(myList, 0, len(myList) - 1))
# print(myList)
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
