# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    a_idx = b_idx = 0
    
    while a_idx < len(arrA) and b_idx < len(arrB):
        if arrA[a_idx] < arrB[b_idx]:
            merged_arr.append(arrA[a_idx])
            a_idx += 1
        else:
            merged_arr.append(arrB[b_idx])
            b_idx += 1
    merged_arr.extend(arrA[a_idx:])
    merged_arr.extend(arrB[b_idx:])
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    a, b = merge_sort(arr[mid:]), merge_sort(arr[:mid])
    return merge(a, b)

merge_sort([6, 7, 2, 5, 1, 9, 10])

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