an_array = [23, 32, 21, 9, 22, 88, 8, 77, 1, 25]
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
    start2 = mid + 1
    
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start = start + 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index = index - 1
            arr[start] = value
            start = start + 1
            mid = mid + 1
            start2 = start2 + 1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l < r:
        m = l + (r - l) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
    return arr

print("Merge_Sort_In_Place: ", merge_sort_in_place(an_array, 0, len(an_array) - 1))

# TO-DO: implement the Quick Sort function below

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            # temp = arr[i]
            # arr[i] = arr[j]
            # arr[j] = temp
            arr[i], arr[j] = arr[j], arr[i]
            
    # temp = arr[i + 1]
    # arr[i + 1] = arr[high]
    # arr[high] = temp
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort( arr, low, high ):
    
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


different_array = [10, 80, 30, 90, 40, 50, 70]
myArr = [1, 5, 7, 8, 10, 3, 12]
print(different_array)
arr = quick_sort(different_array, 0, len(different_array) - 1)
print("Quick_Sort With Different Array: ", arr)
    
# print(quick_sort(an_array, 0, len(an_array) - 1))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
RUN = 32
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:

            arr[j+1] = arr[j]
            j -= 1

        arr[j + 1] = temp

def merge_tim(arr, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:

        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timsort( arr, n ):
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min((i+31), (n - 1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n - 1))
            merge_tim(arr, left, mid, right)
        size = 2*size
    return arr
    
print(myArr)
# print("insertion: ", insertion_sort(myArr))
print("Timmah!: ", timsort(myArr, len(myArr)))