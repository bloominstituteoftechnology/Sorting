# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through from zero to the second to last item in the list, bc the last item will be the highest. when you get there return arr
    for i in range( 0, len( arr ) - 1 ):
        #pivot set to temp var
        cur_index = i
        #loop again comparing the pivot to the other items in the array
        for j in range( i+1, len( arr )):
            # if a number in the array is less than the pivot
            if arr[ j ] < arr[ cur_index ]:
                #reset the pivot to J
                cur_index = j
        #this swaps the order or the sorted array if the num is less than the pivot
        arr[ i ], arr[ cur_index ] = arr[ cur_index ], arr[ i ]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False #pause for check?
        #iterate through to second to last, when you get to the end, return the sorted array
        for n in range( len( arr ) - 1 ):
            #if the pivot is greater that the item next to it in the array
            if arr[ n ] > arr[ n + 1 ]:
                #change positions 
                arr[ n ], arr[ n + 1 ] = arr[ n + 1 ], arr[ n ]
                #change swap back to true so that it can start the loop over
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr