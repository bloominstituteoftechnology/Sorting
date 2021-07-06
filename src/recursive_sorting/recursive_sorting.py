# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arr_1_index = 0
    arr_2_index = 0
    merged_arr_iterator = 0

    while arr_1_index < len(arrA) and arr_2_index < len(arrB):
        if arrA[arr_1_index] < arrB[arr_2_index]:
            merged_arr[merged_arr_iterator] = arrA[arr_1_index]
            merged_arr_iterator += 1
            arr_1_index += 1
        else:
            merged_arr[merged_arr_iterator] = arrB[arr_2_index]
            merged_arr_iterator += 1
            arr_2_index += 1
    while arr_1_index < len(arrA):
        merged_arr[merged_arr_iterator] = arrA[arr_1_index]
        merged_arr_iterator += 1
        arr_1_index += 1
    while arr_2_index < len(arrB):
        merged_arr[merged_arr_iterator] = arrB[arr_2_index]
        merged_arr_iterator += 1
        arr_2_index += 1

    return merged_arr

birthdayArr = [18, 10, 3, 8, 5, 9, 7, 4, 16]
ageArr = [29, 49, 8, 28, 33]
print(merge(birthdayArr, ageArr))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr)>1: 

        banana = int(len(arr)/2) 

        arr_left = arr[:banana] 
        arr_right = arr[banana:] 
        return merge(merge_sort(arr_left), merge_sort(arr_right))

    else:
        return arr

celticJerseyNumbers = [38, 8, 9, 51, 73, 4, 7, 36, 43, 45, 20, 12, 30, 26, 0, 37, 44, 27, 11, 77, 99]
print(merge_sort(celticJerseyNumbers))


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
