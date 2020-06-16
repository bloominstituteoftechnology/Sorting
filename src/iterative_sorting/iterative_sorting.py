# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
    for i in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[i]:
                smallest_index = i   



        # TO-DO: swap

    smallestItem = arr[smallest_index]
    itemToSwap = arr[cur_index]
    arr[cur_index] = smallestItem
    arr[smallest_index] = itemToSwap


    return arr

    print(selection_sort([17, 18, 2, 4, 1, 7, 19, 19, 3, 10]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr