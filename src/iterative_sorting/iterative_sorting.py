# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for i in range(i+1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i

        # TO-DO: swap
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        j = i           #I think this is the currect position if I'm understanding
        while j > 0 and arr[j] < arr[j-1]:        # checking each element to see if it is less
            arr[j], arr[j-1] = arr[j-1], arr[j]    #this is the actual swap
            j -= 1                           #go back to previous element in the list

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr