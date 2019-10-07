# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x  

        # TO-DO: swap
        # Can perform the swap two ways.
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
        # Or do it in a one line swap.
        # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # Two nested for loops, results in a runtime of O(n^2).
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for x in range(i, len(arr)):
            if arr[i] > arr[x]:
                temp = arr[i]
                arr[i] = arr[x]
                arr[x] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr