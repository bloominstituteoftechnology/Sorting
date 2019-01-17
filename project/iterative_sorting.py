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

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
