# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    if i >= len(arrA):
        merged_arr += arrB[j:]
    elif j >= len(arrB):
        merged_arr += arrA[i:]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    length = len(arr)

    # base case
    if length == 2:
        result = [[num] for num in arr]
        return merge(result[0], result[1])

    middle = length // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    i = start
    j = mid + 1

    # already sorted
    if arr[mid] <= arr[j]:
        return
    while i <= mid and j <= end:
        # already in right place
        if arr[i] <= arr[j]:
            i += 1
        else:
            value = arr[j]
            index = j
            # shift all numbers to the right
            while index != i:
                arr[index] = arr[index-1]
                index -= 1
            # Save value in right place
            arr[i] = value
            # Increment all indices after shift
            i += 1
            j += 1
            mid += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if len(arr) <= 1:
        return arr

    #  base case
    if l >= r:
        return arr

    middle = l + (r - l) // 2

    merge_sort_in_place(arr, l, middle)
    merge_sort_in_place(arr, middle+1, r)
    merge_in_place(arr, l, middle, r)
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
