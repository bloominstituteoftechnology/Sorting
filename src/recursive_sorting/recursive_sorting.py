# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( sortLeft, sortRight ):
    elements = len( sortLeft ) + len( sortRight )
    merged_arr = [0] * elements # creates a new array of values 0 with the length 
    # of arr left + arr right
    # TO-DO
    i = 0
    j = 0
    k = 0
    while i < len(sortLeft) and j < len(sortRight):
        if sortLeft[i] < sortRight[j]:
            # reassign the first index of the original array
            merged_arr[k] = sortLeft[i]
            # move to the next value for both the original array and the left array
            i=i+1
            k=k+1
        else:
            # reassign the first index of the original array to the first index of the right array
            merged_arr[k] = sortRight[j]
            j=j+1
            k=k+1
    while i < len(sortLeft):
        merged_arr[k] = sortLeft[i]
        i = i + 1
        k = k + 1
    while j < len(sortRight):
        merged_arr[k] = sortRight[j]
        j = j + 1
        k = k + 1  
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # arrLen = 
    # print(arr)
    if len(arr) < 2:
        return arr
     
    half = len(arr) //2
    print(half)
    left = arr[:half]
    right = arr[half:]

    # call the recursive function again to further divide both arrays
    sortLeft = merge_sort(left)
    sortRight = merge_sort(right)
       
    # to avoid values being left out while merging, check and add the remaining
    # values to the original array
       
    return merge(sortLeft, sortRight)

print(merge_sort([70, 9, 80, 40, 10, 78]))

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
