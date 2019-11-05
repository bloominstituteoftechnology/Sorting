# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    i_of_a, i_of_b = 0, 0
    # TO-DO
    while i_of_a < len(arrA) and i_of_b < len(arrB):
        if arrA[i_of_a] < arrB[i_of_b]:
            merged_arr.append(arrA[i_of_a])
            i_of_a+=1
        else:
            merged_arr.append(arrB[i_of_b])
            i_of_b+=1
    if i_of_a == len(arrA): merged_arr.extend(b[i_of_b:])
    else:                   merged_arr.extend(a[i_of_a:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1: return arr
    L, R = merge_sort(arr[ : len(arr) / 2]), merge_sort(arr[ len(arr) / 2 : ])
    return merge(L,R)


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
