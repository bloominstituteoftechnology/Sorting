# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Find minimum element
        cur_index = i

        # have to not do len(arr) - 1 to access last element
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j

        # Swap minimum element
        x = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = x

    return arr


# TO-DO:  implement the Bubble Sort function below
# bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order
def bubble_sort(arr):
    x = len(arr)

    for i in range(x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
