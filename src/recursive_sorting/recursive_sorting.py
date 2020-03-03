# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        #compare the two values, choose the smaller one
        if (arrA[i] <= arrB[j]):
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    
    return merged_arr + arrA[i:] + arrB[j:]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base (Easiest case)
    if len(arr) <= 1:
        return arr

    # devide the arrays
    half = len(arr) // 2
    left = merge_sort(arr[0:half])
    right = merge_sort(arr[half:])

    #merging sorted arrays
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
