# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for smallest_index in range(i+1, len(arr) ):
            if arr[cur_index] > arr[smallest_index]:
                cur_index = smallest_index
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
#1 compare first two items
#2 if the left > right, swap (1st item is sorted, everything else is not)
#3 next two items, repeat above step
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1): #outer for loop
       for j in range(0, len(arr) - 1 - i): #inner for loop
           if arr[j] > arr[j+1]: #compare item with item on right
               arr[j], arr[j+1] = arr[j+1], arr[j] 
                #if item on left > item on right, swap
    return arr




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr