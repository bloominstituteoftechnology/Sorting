# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):

    for i in range(0, len(arr)):
        
        # # save element to sort
        smallest_index = i

        # iterate to the left of the element to find the smallest list element        
        for x in range(i+1, len(arr)):

            if arr[smallest_index] > arr[x]:
                smallest_index = x
        
        # switch the current and smallest elements
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # set initial condition for swaps to execute
    swaps = 1

    while swaps > 0:
        #holder to count actual swaps
        temp_swaps = 0

        for i in range(0, len(arr)-1):

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                temp_swaps += 1
        swaps = temp_swaps

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    if len(arr) == 0:
        return []

    # 1 empty array for counts
    count = [0 for x in range(max(arr)+1)]

    # 2 count every element of input array
    for i in range(0, len(arr)):
        
        #screen for negatives
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[arr[i]] = count[arr[i]] + 1


    # 3 add up elements
    for x in range(1, len(count)):
        count[x] = count[x] + count[x-1]
    
    
    # 4 put elements into the result array
    result = [0 for x in range(0, len(arr))]

    for j in range(0, len(arr)): 

        result[count[arr[j]]-1] = arr[j]
        count[arr[j]] = count[arr[j]] - 1

    return result