# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        half = len(arr) // 2
        arrL = arr[half:]
        arrR = arr[:half]
        left = merge_sort(arrL)
        right = merge_sort(arrR)
        arr = merge(left, right)

    return arr

def merge_in_place(arr, start, mid, end):
    # TO-DO
    i = mid + 1
    if arr[mid] <= arr[i]:
        return arr

    while start <= mid and i <= end:
        if arr[start] <= arr[i]:
            start += 1
        else:
            val = arr[i]
            j = i

            while j != start:
                arr[j] = arr[j - 1]
                j -= 1

            arr[start] = val

            start += 1
            mid += 1
            i += 1

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
