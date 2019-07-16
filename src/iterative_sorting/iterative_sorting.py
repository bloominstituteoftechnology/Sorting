# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        # Find next smallest element
        smallest_index = i
        for x in range(i+1,len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        #Easier to read but less efficient.
        #Searches unsorted list twice first to find min value
        #Then again in order to find the index
        '''
        #Get smallest index of unsorted list
        unsorted_list = arr[i:]
        smallest_index = arr.index(min(unsorted_list)) 
        '''  
        
        # Swap min value to current index
        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Starting from the first array element
    i = 0
    #While i < length of array minus one
    while i < len(arr)-1: 
        if arr[i+1] < arr[i]:
            #If the next array element is smaller than the current element
            #Then swap them and reset index to 0
            arr[i],arr[i+1] = arr[i+1], arr[i]
            i = 0
        else:
            #Else increment i
            i += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr