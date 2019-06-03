# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                smallest_index = j; 
                temp_val =arr[i] 
                arr[i] = arr[j]
                arr[j] = temp_val
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            val = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = val
            swapped = True
            bubble_sort(arr)
    return arr

print(bubble_sort([6,5,4, 103, 44, 55, 3,2,1]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr