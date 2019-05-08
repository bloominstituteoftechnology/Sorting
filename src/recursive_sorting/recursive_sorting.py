test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# O(n)
# Helper function merges 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # initialize indices for accessing elements in the two arrays
    a = 0
    b = 0

    # Loop through list of elements
    for i in range(elements):
        
        # if all elements from arrA have been merged
        if a >= len(arrA):
            # put next element in arrB into merged array
            merged_arr[i] = arrB[b] # Could use append if started with merged_arr = []
            b += 1

        # if all elements from arrB have been merged
        elif b >= len(arrB):
            # put next element in arrA into merged array
            merged_arr[i] = arrA[a]
            a += 1

        # if A[0] is smaller than B[0]
        elif arrA[a] < arrB[b]:
            # put the element from A into the output array
            merged_arr[i] = arrA[a]

            # increment the index
            a += 1

        # if A[0] is bigger than B[0]
        else: # arrA[a] >= arrB[b]:
            # put the element from B into the output array
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# O(n log(n)) - we are doing an O(n) function (splitting the initial array in half), log(n) times
# Implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    # Base Case
    # While data set contains more than one item, split it in half
    if len(arr) > 1:

        # Recursive Case
        # Recursively call merge_sort to continue splitting the arrays in half
        left_partition = merge_sort(arr[:len(arr) // 2])
        right_partition = merge_sort(arr[len(arr) // 2:])

        # Merge the left and right sides together into one array
        arr = merge(left_partition, right_partition)

    return arr

print(merge_sort(test))






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
