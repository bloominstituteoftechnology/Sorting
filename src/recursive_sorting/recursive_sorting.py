# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    first_i = 0
    second_i = 0

    while first_i < len(arrA) and second_i < len(arrB):

        if arrA[first_i] < arrB[second_i]:
            merged_arr.append(arrA[first_i])
            first_i += 1
        else:
            merged_arr.append(arrB[second_i])
            second_i += 1

    merged_arr.extend(arrA[first_i:])
    merged_arr.extend(arrB[second_i:])

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
################################################################
arr = [5, 4, 8, 7, 9, 2, 5, 3]


def merge_sort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr
    # define where to split
    split_point = len(arr) // 2

    # set up splits
    #first try DOES NOT WORK
    # left_set = arr[:split_point]
    # right_set = arr[split_point:]
    left_set = merge_sort( arr[ :split_point] )
    right_set = merge_sort( arr[ split_point: ] )

    # sanity check
    print("left set  = ~~~>", left_set)
    print("right set = ~~~>", right_set)

    # calling merge_sort recursively// this does not work, it needed to be run in initial split above
    # merge_sort(left_set)
    # merge_sort(right_set)

    # Use the Merge Helper function
    print('merged list', merge(left_set, right_set))
    return merge(left_set, right_set)


merge_sort(arr)

print('\n'+"Sorted arr ~~~>",merge_sort(arr),'\n')
print("Original array ~~~>", arr)
print('\n~~~ merge_sort function ends ~~~~')


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#     return arr
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
# return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     return arr
