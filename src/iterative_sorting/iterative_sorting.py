import numpy as np


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
             if arr[j] < arr[smallest_index]:
                 smallest_index = j

        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = \
                arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    num_swaps = 1
    while num_swaps != 0:
        num_swaps = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                num_swaps += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    #Find the maximum value:
    if maximum == -1:
        try:
            maximum = max(arr)
        except ValueError:
            return []
    
    # Store the count of each unique object.
    count = np.zeros(maximum + 1)
    for num in arr:
        if num < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        count[num] += 1
    
    # Make the count array cumulative.
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    output_arr = arr.copy()
    for num in arr:
        output_arr[int(count[num]) - 1] = num
        count[num] -= 1
        
    return output_arr