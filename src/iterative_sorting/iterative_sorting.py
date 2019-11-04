# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_num = arr[i]
        smallest_num = cur_num
        lowest_index = i
        for num in range(i, len(arr)):
            if arr[num] < smallest_num:
                smallest_num = arr[num]
                lowest_index = num
        arr[i], arr[lowest_index] = smallest_num, cur_num
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    ready_to_test = True
    while ready_to_test:
        ready_to_test = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                ready_to_test = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr