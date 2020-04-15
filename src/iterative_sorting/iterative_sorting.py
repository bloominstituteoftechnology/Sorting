# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

    # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted  
    # - Shift items over to the right as you iterate

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

    # c. When the correct index is found, copy temp into this position
        # TO-DO: swap

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    return arr



    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

# make flag to show if swap has occured
    swaps_occured = True
    # Run until no swaps
    while swaps_occured:
        swaps_occured = False
    
    #for each element in the array...
        for i in range(len(arr) - 1):

        # check neighbor to the right
            if arr[i] > arr[i+1]:
        
        # if neighbor is smaller, swap and make flag true
                arr[i],  arr[i+1] =  arr[i+1], arr[i]
                swaps_occured = True

    return arr







# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr