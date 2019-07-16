# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range( 0, len( arr ) - 1 ):
        cur_index = i
        for j in range( i+1, len( arr )):
            if arr[ j ] < arr[ cur_index ]:
                cur_index = j
        arr[ i ], arr[ cur_index ] = arr[ cur_index ], arr[ i ]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for n in range( len( arr ) - 1 ):
            if arr[ n ] > arr[ n + 1 ]:
                arr[ n ], arr[ n + 1 ] = arr[ n + 1 ], arr[ n ]
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr