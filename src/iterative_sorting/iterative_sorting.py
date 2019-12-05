# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        for x in range (i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x



        # TO-DO: swap
        y = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = y



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr