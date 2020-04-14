# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i #
        smallest_index = cur_index
        # TO-DO: find next smallest element, (x, y = y, x)
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j     


        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # For each element in the array...
        for j in range(n - 1 - i):
            # Check it's neighbor to the right...
            if arr[j] > arr[j + 1]:
                # If neighbor is smaller, swap and make Flag true
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    return arr