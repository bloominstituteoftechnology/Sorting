# TO-DO: Complete the selection_sort() function below 
sumArr = [ 5, 6, 3, 8, 10, 12, 15, 1, 4]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range( 0, len( arr ) - 1):
        cur_index = i
        smallest_index = cur_index #Saves the current smallest index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for smallest_index in range(i + 1, len(arr)): #Here we iterate over smallest index list
            if arr[cur_index] > arr[smallest_index]:
              cur_index = smallest_index
          
    # TO-DO: swap
        tempList = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = tempList

    return arr

selection_sort(sumArr)
# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr