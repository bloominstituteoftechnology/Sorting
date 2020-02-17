# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if (arr[smallest_index] > arr[j]):
                smallest_index = j


        if(arr[cur_index] > arr[smallest_index]):
            lowest = arr[smallest_index]
            highest = arr[cur_index]
            arr[cur_index] = lowest
            arr[smallest_index] = highest



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        did_swap = False
        for i in range(0, len(arr) - 1):
            next_index = i + 1
            if arr[i] > arr[next_index]:
                lowest = arr[next_index]
                highest = arr[i]
                arr[i] = lowest
                arr[next_index] = highest
                did_swap = True
        if not did_swap: break
            
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr