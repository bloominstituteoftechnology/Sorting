# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        if(arr[i] < arr[smallest_index]):
            smallest = i
        # TO-DO: swap
            a = i
            b = smallest
            arr[a], arr[b] = arr[b], arr[a]
    return print(arr)

selection_sort([7,5,1,4,2])
# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
