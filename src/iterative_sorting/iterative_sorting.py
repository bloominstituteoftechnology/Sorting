# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop through the list to the right of i
        for j in range (i, len(arr)): 
            #check each item against the smallest_index
           if arr[j] < arr[smallest_index]:
               # if the item at is smaller than the one at smallest index, set smallest index to j
               smallest_index = j
        
        # TO-DO: swap
        # once the index of the smallest item in the list has been found, assign its value to arr[i] from the outer loop

        big = arr[i]
        small = arr[smallest_index]
        arr[i] = small
        arr[smallest_index] = big



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
