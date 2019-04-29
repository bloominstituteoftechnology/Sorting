# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    return arr

selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0 , len(arr) -1):
            if arr[i] > arr[i + 1]:
                swapped = True
                h = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = h
    print(arr)
    return arr

bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr