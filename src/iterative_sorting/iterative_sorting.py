# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for num_of_scan in range(0, len(arr)):
        for i in range(0, len(arr) - num_of_scan - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)
    return arr

# bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr