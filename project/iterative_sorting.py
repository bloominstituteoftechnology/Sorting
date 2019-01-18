# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # iterate through the list to compare
        for c in range(cur_index, len(arr)):
            # compare to find the smallest number
            if arr[c] < arr[smallest_index]:
                smallest_index = c

        # TO-DO: swap
        # save the element to switch
        switch = arr[smallest_index]
        # switch one of the elements
        arr[smallest_index] = arr[cur_index]
        # complete the switch
        arr[cur_index] = switch

    return arr

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # create a for loop for from the first index through the length of the array
    for i in range(1, len(arr)-1):
        # number to compare to
        mover = arr[i] # starts at 1
        # create the entry point for the sorted cards to start filling in
        list_comp = i - 1 # starts at 0
        # check to be sure the index is above zero and less then the number in at the sorted end of the array
        # while that is true continue through the list
        while list_comp >= 0 and mover < arr[list_comp]:
            # shift the item left into space matching condition
            arr[list_comp + 1] = arr[list_comp]
            # as i increments forward decrement list_comp to keep it one behind to continue to compare
            list_comp -= 1
        # shift item to the right
        arr[list_comp + 1] = mover 
    return arr

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
