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
        
        # set the first unsorted element as the minimum
        # for each of the unsorted elements
        # if element < currentMinimum
        # set element as new minimum
        # swap minimum with first unsorted position
        if arr[cur_index + 1 ] < arr[cur_index]:
            arr[smallest_index] = arr[cur_index + 1]



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr