# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for indx in range(0, len(arr) - 1):
        cndx = indx
        sndx = cndx
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for xndx in range(indx+1, len(arr)):
            if arr[sndx] > arr[xndx]:
                sndx = xndx

        # TO-DO: swap
        tndx = arr[indx]
        arr[indx] = arr[sndx]
        arr[sndx] = tndx


    return arr


print(selection_sort([5,2,7,4,9,10,3,1,0,34]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr