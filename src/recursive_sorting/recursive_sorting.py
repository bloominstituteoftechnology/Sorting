l = [1, 5, 8, 4, 2, 9, 6, 0, 10, 3, 7]


# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #print(f"elements: {arrA} and {arrB} - merged_arr {merged_arr}")

    a = 0
    b = 0
    i = 0

    while i < len(merged_arr):
        if a > len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b > len(arrB):
            merged_arr[i] = arrB[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        i += 1
    return merged_arr

# half = len(l)//2
# x = merge(l[:half], l[half:])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if (len(arr) == 1):
        return arr
    else:
        half_len = len(arr)//2
        # get first half
        left_arr = l[:half_len]
        # get second half
        right_arr = l[half_len:]

        left_sorted = merge_sort(right_arr)
        right_sorted = merge_sort(left_side)



    return merge(left_sorted, right_sorted)




# print(l[:len(l)//2])
# print(l[len(l)//2:])


print(merge_sort(l))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
