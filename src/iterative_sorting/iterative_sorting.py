# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i 
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
            # i + 1 makes it so we start at 1 and not 0, b/c lists, aka arrays start at 0.
        for j in range(i + 1, len(arr)): # i + 1 = 0 + 1, length(arr)
            if arr[j] < arr[smallest_index]:  # j ( is less than) smallest_index (1)
                smallest_index = j # 1 = 1


        # TO-DO: swap

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # 0, 0 = 0, 0


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #length of list (array)
    bubble = len(arr) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, bubble):
            #item on left greater than item on right, set sorted to false, flip items.
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr