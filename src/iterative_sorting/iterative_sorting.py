# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]: 
                smallest_index = j

        # TO-DO: swap
        if cur_index != smallest_index:
            temp = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = temp


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



selection_sort([1,2,4,5,6,0, 30, 23,21])
bubble_sort([1,2,4,5,6,0, 30, 23,21])