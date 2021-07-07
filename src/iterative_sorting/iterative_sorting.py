# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i 
        smallest_index = cur_index
        #One pass from cur_index to the value before the last one
        # try to find index of the smallest element
        for j in range(i + 1, len(arr)):
           if arr[smallest_index] > arr[j]:
               smallest_index = j
        #swap value at cur_index with the smallest element found at smallest_index
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    return arr
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        #number of swaps done during a pass
        swaps = 0
        # One pass swapping adjacent values
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i+1] = temp
                swaps = swaps + 1
        #if no swaps was done during the pass then the array is sorted
        if swaps == 0:
            break
    return arr
# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#     return arr