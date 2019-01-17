# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]





    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    i  = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j - 1
        #end of nested while 
        arr[j+1] = x
        i = i + 1 
    #end of parent while loop 
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    """
    O(n^2) time complexity
    should be used with smaller lists 
    can be used with semi sorted lists. 
    arr must be an iterable perferably an array type. 
    Will sort in ascending order. 
    """
    for element in arr:
        for index in range (len(arr) - 1):
        if arr[index] > arr[index + 1]:
            arr[index], arr[index+1] = arr[index+1], arr[index]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr