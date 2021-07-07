# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    for x in range(elements + 1):
        if i < len(arrA) and j < len(arrB):
            if arrA[i] >= arrB[j]:
                merged_arr.append(arrB[j])
                j += 1
            else:
                merged_arr.append(arrA[i])
                i += 1
        elif i >= len(arrA) and j < len(arrB):
            merged_arr.append(arrB[j])
            j += 1
        elif j >= len(arrB) and i < len(arrA):
            merged_arr.append(arrA[i])
            i += 1
        else:
            break
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
