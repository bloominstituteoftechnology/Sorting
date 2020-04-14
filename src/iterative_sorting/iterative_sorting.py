# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        min_val = min(arr[cur_index+1: ])
        min_index = arr.index(min_val)
        if min_val < arr[cur_index]:
            arr[min_index]= arr[cur_index]
            arr[cur_index] = min_val
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while arr != sorted(arr):
        for i in range(0, len(arr) - 1):
            left = arr[i]
            right = arr[i+1]
            if left > right:
                arr[i], arr[i+1] = right, left
    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr