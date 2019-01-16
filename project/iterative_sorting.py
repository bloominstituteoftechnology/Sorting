# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                # Swap the found minimum element with the first element
                # if it is smaller than current smallest_index
                smallest_index = j
                # switches index value not the actual number itself
        #  This swaps initial value (first value) with new smallest value
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)-1):
        key = arr[i]
        shift = i - 1
        while shift >= 0 and key < arr[shift]:
            arr[shift + 1] = arr[shift]
            shift -= 1
        arr[shift + 1] = key
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr