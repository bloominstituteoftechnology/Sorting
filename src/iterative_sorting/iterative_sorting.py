# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    ref = arr.copy() # create a reference point 
    arrLen = int(len(arr))
    print(arr)
    for i in range(arrLen - 1):
        if arr[i] < arr[i + 1]: # if the starting value is less than the adjacent value
            pass # pass over it
        elif arr[i] > arr[i + 1]: # if current value is greater than the adjacent value
            a = arr[i] # store index value in variable
            b = arr[i + 1] # store index + 1 value in variable
            # organize the values by "swapping"
            arr.pop(i)
            arr.insert(i, b) 
            arr.pop(i + 1)
            arr.insert(i + 1, a)
    if ref == arr:
        print('Array is sorted!')
    elif ref != arr:
        bubble_sort(arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr