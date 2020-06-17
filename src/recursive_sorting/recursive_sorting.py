# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(merged_arr)
    print(elements)
    # TO-DO
    if arrA[0] < arrB[0]:
        arrA.append(arrB[0])
        return arrA
    else:
        arrB.append(arrA[0])
        return arrB


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr, sorted_array):
    if len(arr) <= 1:
        if len(sorted_array) == 0:
            sorted_array.append(arr[0])
            return
        else:
            for i in range(0, len(sorted_array)):
                if arr[0] < sorted_array[i]:
                    sorted_array.insert(i, arr[0])
                    arr.clear()
                    return
                elif i == len(sorted_array) - 1:
                    sorted_array.append(arr[0])
                    return
    left_side = arr[: int(len(arr) / 2)]
    right_side = arr[int(len(arr) / 2):]
    if len(arr) >= 2:
        merge_sort(left_side, sorted_array)
        merge_sort(right_side, sorted_array)

    print(sorted_array)

merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7], [])


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
