# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element (hint, can do in 3 loc) 

        # First, I need to iterate through the elements that remain in the arr

        for x in range(smallest_index + 1, len(arr)):
        
            # Second, I need to check if the element is smaller than the currently smallest
        
            if arr[x] < arr[smallest_index]:
        
                # Third, if this statement is True, I will need to set the new index to be the smallest
        
                smallest_index = x

        # TO-DO: swap the arr

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr