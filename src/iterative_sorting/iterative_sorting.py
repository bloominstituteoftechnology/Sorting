# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        if smallest_index != cur_index:
            val = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = val
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        cont = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                cont = True
                val = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = val
        if not cont:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    count_arr = [0] * maximum
    for a in arr:
        count_arr += 1
    init = 0
    for ind, val in enumerate(count_arr):
        for a in range(val):
            arr[init] = ind
            init += 1
    return arr