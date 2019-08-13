# TO-DO: Complete the selection_sort() function below 
arr = [64, 25, 12, 22, 11]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  #iterate over list to find smallest item, set that as current index
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for n in range(cur_index, len(arr)):  #iterate again to look at grab the item next to current index
            if arr[n] < arr[smallest_index]:  #compare, if next item is less then current index
                smallest_index = n              #set next item as the new current index by swap

        # TO-DO: swap
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr

selection_sort(arr)
print(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        j = i           #I think this is the currect position if I'm understanding
        while j > 0 and arr[j] < arr[j-1]:        # checking each element to see if it is less
            arr[j], arr[j-1] = arr[j-1], arr[j]    #this is the actual swap
            j -= 1                           #go back to previous element in the list

    return arr


# STRETCH: implement the Count Sort function below
#def count_sort( arr, maximum=-1 ):

  #  return arr