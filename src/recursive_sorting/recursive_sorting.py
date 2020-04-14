# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # initial list
    merged_arr = []
    # initial index for left array
    leftIdx = 0
    # initial index for right array
    rightIdx = 0

    # TO-DO
    # iterate while both lists have more than one element left
    while(leftIdx < len(arrA) and rightIdx < len(arrB)):
        # if el in right array is more than el in left 
        if(arrB[rightIdx] > arrA[leftIdx]):
            # append el in left arr to merged_arr
            merged_arr.append(arrA[leftIdx])
            # increase by one left arr index to move to next el
            leftIdx += 1
        else:
            merged_arr.append(arrB[rightIdx])
            rightIdx += 1
    
    # if either array is still unsorted, pass each element till no element is left
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
    # if length of arr is less or equal to 1 return arr
    # BASE CASE for recursive function
    if(len(arr) <= 1):
        return arr

    # find the middle
    half = len(arr) // 2
    # divide arr into 2 parts, left and right split by middle using slice
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    # return the left and right list merged together
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
