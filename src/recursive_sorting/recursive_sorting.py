# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # start at the first element of each array
    indexA = indexB = indexMerged = 0

    # while there are still values in both (arrA and arrB)
    while indexA < len(arrA) and indexB < len(arrB):
        # if the value in arrayA is smaller or equal than arrayB:
        if arrA[indexA] <= arrB[indexB]:
            # save value(arrA) in the merged array
            merged_arr[indexMerged] = arrA[indexA]
            # incriment the the index because we already use it
            indexA += 1
        else:
            # save value(arrB) in the merged array
            merged_arr[indexMerged] = arrB[indexB]
            # incriment the the index because we already use it
            indexB += 1
        # increment the index of merged because we filled that spot
        indexMerged +=1
    # while there elements just in one of the arrays:
    while indexB < len(arrB):
        # add the final elements that are inside the arrayB in the merged array
        merged_arr[indexMerged] = arrB[indexB]
        indexB += 1
        indexMerged += 1
    while indexA < len(arrA):
         # add the final elements that are inside the arrayA in the merged array
        merged_arr[indexMerged] = arrA[indexA]
        indexA += 1
        indexMerged += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Base case: arr length 0 or 1
    if len(arr) <= 1:
        return arr
    # Otherwise:
    else:
        # Find middle or array with // 2
        middle = len(arr)//2
        # Divide 
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        arr = merge(left, right)
        return arr
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
