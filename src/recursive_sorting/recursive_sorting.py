# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # prepopulating array with zeroes so it runs faster
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    # while the left and right arrays still have items
    while arrA and arrB:
        left_list_item = arrA[0]
        right_list_item = arrB[0]

        if(left_list_item < right_list_item):
            merged_arr.append(left_list_item)
            arrA.pop(0)
        else:
            merged_arr.append(right_list_item)
            arrB.pop(0)



    while arrA:
        merged_arr.append(arrA[0])
        arrA.pop(0)


    while arrB:
        merged_arr.append(arrB[0])
        arrB.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    list_len = len(arr)
    # TO-DO
    if (list_len < 2):
        return arr

    left = arr[:list_len // 2]
    right = arr[list_len // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


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

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(merge_sort(arr1))