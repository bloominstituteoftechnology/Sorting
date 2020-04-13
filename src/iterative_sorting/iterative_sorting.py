# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i,len(arr)):
            if(arr[x] < arr[smallest_index]):
                smallest_index = x
    
        # TO-DO: swap
        t = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = t

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len( arr )-1):
        for x in range(0, len( arr )-1):
            if(arr[x] > arr[x+1]):
                t = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = t

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if(len(arr) == 0):
        return arr
    elif(any([True if x < 0 else False for x in arr])):
        return "Error, negative numbers not allowed in Count Sort"
    
    # Make counting list of length = largest integer in arr
    count_arr = [0]*(max(arr)+1)
    out_arr = [0]*(len(arr))

    # Count instances of each numberin the counting list
    for x in arr:
        count_arr[x] = count_arr[x] + 1

    for x in range(0,len(count_arr)-1):
        count_arr[x+1] = count_arr[x+1] + count_arr[x]

    for x in arr[::-1]:
        index = count_arr[x] - 1
        out_arr[index] = x

    arr = out_arr

    return arr