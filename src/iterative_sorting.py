# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        current_index = i
        min_value_index = current_index
        for j in range(current_index, len(arr) - 1):
            if arr[min_value_index] > arr[j]:
                min_value_index = j
        temp = arr[min_value_index]
        arr[min_value_index] = arr[current_index]
        arr[current_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapping_occured = True
    while swapping_occured:
        swapping_occured = False
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            swapping_occured = True
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
