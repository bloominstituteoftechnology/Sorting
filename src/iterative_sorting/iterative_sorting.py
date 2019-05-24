# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        # TO-DO: swap
        swap = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = swap



    return arr
    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for x in range (0, len(arr)):
            for y in range (0, len(arr) - x - 1):
                if arr[y] > arr[y+1]:
                    arr[y], arr[y+1] = arr[y+1], arr[y]
                    swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr