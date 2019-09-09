# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        curr = i
        smallest = curr
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # iterate over each item in the array; start at curr number, stop at len(arr)
        for x in range(curr, len(arr)):
            # if number is smaller than curr, set smallest to number
            if arr[x] < arr[smallest]:
                smallest = x



        # TO-DO: swap
        # move to next number
        temp = arr[smallest]
        arr[smallest] = arr[curr]
        arr[curr] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr