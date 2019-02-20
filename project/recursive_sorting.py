# helper function


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
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# some_arr = [4, 22, 15, 53, 65, 33, 23, 45, 12, 7, 10, 17, 27, 48, 66]
# print(some_arr)
# print(merge_sort(some_arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
# pivot
# quicksort(a as arr, low as int, high as int)
# if low < high , pivot location assigned to function Partition(arr, low, high)
# quicksort(a, low, pivot location)
# quicksort(a , pivot location plus 1 , high)
# partition (a , low as int, high as int)
# pivot = A[low]
# leftwall = low
# for i = low + 1 to high
# if a[i] < pivot then swap a[i] with a[leftwall]
# leftwall = leftwall + 1
# swap(pivot, a[leftwall])
# return leftwall

# [7,9,0,4,2,8,6,1,3,5] pivot = 5, elements less than 5 move to left, elements greater than 5 move to right
# 1[3,9,0,4,2,8,6,1,7,5], 2[3,1,0,4,2,8,6,9,7,5], 3[3,1,0,4,2,8,6,9,7,5], 4[3,1,0,4,2,8,6,9,7,5], 5[3,1,0,4,2,8,6,9,7,5], 6[3,1,0,4,2,5,6,9,7,8], 7[3,1,0,4,2,5,6,9,7,8], 8[3,1,0,4,2,5,6,8,7,9]
# partitioned arrays [3,1,0,4,2] pivot 2 and [6,8,7,9] pivot 9
# 1[0,1,3,4,2], 2[0,1,3,4,2], 3[0,1,2,4,3] // 1[6,8,7,9], 2[6,8,7,9], 3[6,8,7,9]
# partitioned arrays [0,1] pivot 1 and [4,3] pivot 3 // [6,8,7] pivot 7
# 1[3,4] // 1[6,8,7] 2[6,7,8]
# [6,8,2,5,9,1,0,3,4,7] pivot = 7, elements less than 7 move to left, elements greater than 7 move to right
# 1[6,8,2,5,9,1,0,3,4,7], 2[6,4,2,5,9,1,0,3,8,7], 3[6,4,2,5,9,1,0,3,8,7], 4[6,4,2,5,9,1,0,3,8,7], 5[6,4,2,5,3,1,0,9,8,7], 6[6,4,2,5,3,1,0,9,8,7], 7[6,4,2,5,3,1,0,9,8,7], 8[6,4,2,5,3,1,0,7,8,9]
# partitioned arrays [6,4,2,5,3,1,0] pivot 0 and [8,9]
# exit recursion when ar length is 1

a_arr = [7, 9, 0, 4, 2, 8, 6, 1, 3, 5]


def quick_sort(arr, low, high):
    # first select a pivot
    # rearrange the arr so that elements less than pivot are to the left, elements greater than the pivot are to the right
    # use partitioning to divide the array

    # must have base condition, exit condition or will have an infinite recursive function, exit if segment has only one element, or start and end is invalid
    # if start of segment is >= end of segment, return , or start < end
    # for case when segment == 1 or invalid segment where no segment is available left of pivot
    if low < high:
        p_index = partition(arr, low, high)
    # partition function returns the index of the partition after sorting the two segments (p-index)
    # once we have returned the p-index make two recursive calls of quick_sort, one to sort the segment left of p-index, and one to sort the segment right of p-index
        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)
    return arr


def partition(arr, low, high):
    # assign pivot to an arbitrary index, choose end position
    pivot = arr[high]
    # start partition_index at index low, this value will be swapped as we traverse the array and while traversing if the index is smaller than p_index
    p_index = low
    # for index in range low to high
    for i in range(low, high):
        # if element at index i is <= pivot, swap element at index i with element at partition_index
        if arr[i] <= pivot:
            # swap, assign element at index to p_index
            temp = arr[i]
            arr[i] = arr[p_index]
            # swap, assign element at p_index to element at index
            arr[p_index] = temp
            # increment partition index to account for swap and placement of pivot
            p_index += 1
            print(i)
            print(f" arr at i, {arr[i]} arr at p index: {arr[p_index]}")
        # swap, assign the element at p_index to element at element of pivot
    temp = arr[p_index]
    arr[p_index] = pivot
    # swap, assign the element at the pivot to element at p_index
    # pivot = temp
    arr[high] = temp
    # return the partition index
    print(p_index)
    return p_index

    [7, 9, 0, 4, 2, 8, 6, 1, 3, 5]


print(quick_sort(a_arr, 0, len(a_arr)-1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
