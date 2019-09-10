# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) \
        for x in range(i + 1, len(arr)):
            if arr[x] < arr[cur_index]:
                cur_index = x
        # TO-DO: swap
        if cur_index != i:
            arr[cur_index], arr[i] = arr[i], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arrLen = len(arr)

    for x in range(0, arrLen - 1):
        swapped = False

        for y in range(0, arrLen - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                swapped = True
        
        if swapped == False:
            break

    

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr