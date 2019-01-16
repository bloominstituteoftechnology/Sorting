# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp     

        # TO-DO: swap

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    ''' 
       seperate first element from rest of array
       begin at index 1
       put that element in a variable
       iterate over subarray for position to insert variable
       shift items in subarray to right to make room for var
       when index is found 
    '''
    for i in range(1, len(arr)):
        currval = arr[i]
        position = i

        while position > 0 and arr[position-1] > currval:
            arr[position] = arr[position-1]
            position = position - 1
        arr[position] = currval

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    ''' 
        loop through length of arr -1
        if arr[i] is greater than arr[i+1]
        assign arr[i] to temp var
        move arr[i+1] down 1
        iterate until sorted

    '''
    for numpass in range(len(arr) -1, 0, -1):
        for i in range(numpass):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr