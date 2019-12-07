# TO-DO: Complete the selection_sort() function below 
def selection_sort( array ):
    # loop through n-1 elements
    for min_index in range(len(array)):
        # TO-DO: find next smallest element
        min_value_index = min_index
        # (hint, can do in 3 loc) 
        for current_index in range(min_index + 1, len(array)):
            if array[current_index] < array[min_value_index]:
                min_value_index = current_index
        # TO-DO: swap
        array[min_index], array[min_value_index] = array[min_value_index], array[min_index]
    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr