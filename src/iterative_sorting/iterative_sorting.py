# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # we are looping through each item in our collection one at a time
    # 0 is the starting number of the index
    # we say -1 here as we have only one item in the list we dont want to do a comparison
    # instead we can assume that is the highest value as it it the last one
    for i in range(0, len(arr) - 1):
        # taking in account the smallest argument comparing with the largest on
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # so all elements to the right of the position (cur_index = i)
        for j in range(i+1, len(arr)):
            # if arr in the position j is less than our smallest_index
             if arr[smallest_index] > arr[j]:
                # then we need to replace our smallest_index with j
               smallest_index = j
             
        # TO-DO: swap
        # at the end before our loop we swap the argument located in the current index 
        # with the smallest item we locate during our loop
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr