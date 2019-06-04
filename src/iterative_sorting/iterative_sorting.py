# Reading material for sorting: 
# https://github.com/carlos-gutier/Sorting/tree/master/src/iterative_sorting

# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for each in range(cur_index, (len(arr))):
            if arr[each] < arr[smallest_index]:
                smallest_index = each
        # temporarely saving smallest number
        temp_small = arr[smallest_index]
        # swapping smallest num found to current idx num
        # and viceversa
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_small
        
    return arr
def bubble_sort( arr ):
    def bubble_sort(arr):
    new_arr = None # to compare with original array
    while True: # loop until no more swaps performed
        for i in range(0, len(arr) - 1):
            left = arr[i]
            right = arr[i+1]
            # if left element is greater than right
            # the swap places
            if arr[i] > arr[i+1]:
                left = arr[i+1]
                right = arr[i]
            arr[i] = left
            arr[i+1] = right
        # break once "new_array" is equal to copy original
        if new_arr == arr:
            return arr
        # making "new_array" equal to copy of original
        new_arr = arr.copy()


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr