# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    leftIdx = 0
    rightIdx = 0

    # TO-DO
    while(leftIdx < len(arrA) and rightIdx < len(arrB)):
        if(arrB[rightIdx] > arrA[leftIdx]):
            merged_arr.append(arrA[leftIdx])
            leftIdx += 1
        else:
            merged_arr.append(arrB[rightIdx])
            rightIdx += 1
    
    while(leftIdx < len(arrA)):
        merged_arr.append(arrA[leftIdx])
        leftIdx += 1

    while(rightIdx < len(arrB)):
        merged_arr.append(arrB[rightIdx])
        rightIdx += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) <= 1):
        return arr

    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

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
