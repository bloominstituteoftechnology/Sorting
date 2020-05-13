# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
             if arr[j] < arr[smallest_index]:
                 smallest_index = j

        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = \
                arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    num_swaps = 1
    while num_swaps != 0:
        num_swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                num_swaps += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr