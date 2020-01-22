# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Add lengths of arrA and arrB to get length needed for new array
    elements = len(arrA) + len(arrB)
    # Create new array of zeros with length of elements
    merged_arr = [0] * elements
    # Create pointer variables
    i = j = k = 0
    while i < len(arrA) and j < len(arrB):
        # Check if value at index i in arrA is smaller or equal to
        # the value at the corresponding index of arrB
        if arrA[i] < arrB[j]:
            # If True, add value at index i in arrA to merged_arr at
            # index k
            merged_arr[k] = arrA[i]
            # Increment i since we used that value already
            i += 1
        else:
            # Add value at index j in arrB to merged_arr at index k,
            # otherwise.
            merged_arr[k] = arrB[j]
            # Increment j since we used that value alread
            j += 1
        # Increment k since we filled that slot in merged_arr
        k += 1
    # If we run out of elemnts in arrA or arrB, we need to
    # continue adding the elements from the other array to
    # merged_arr and increment accordingly.
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    else:
        # Cut array in half
        middle = len(arr) // 2

        # Create 2 new arrays to be passed recursively to the merge() function
        # Recursively call the merge_sort() function on left and right
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        # Merge the two arrays
        arr = merge(left, right)

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
def timsort(arr):

    return arr
