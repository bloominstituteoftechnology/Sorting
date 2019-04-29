# TO-DO: Complete the selection_sort() function below 
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
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp


    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    swaps = True
    while swaps:
        swaps = False
        for i in range(0, len(arr) - 1):
            first = arr[i]
            second = arr[i+1]

            if first > second:
                arr[i] = second
                arr[i+1] = first
                swaps = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Validate Inputs
    if len(arr) < 2:
        return arr

    if maximum == -1:
        maximum = max(arr)

    # Set up variables    
    count = [0 for x in range(maximum+1)]
    result = [0 for x in range(len(arr))]

    # Count elements
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Set each element at the right place
    for num in arr:
        result[count[num]-1] = num
        count[num] -= 1

    return result

'''Bogo sort is an incredibly inefficient algorithm that basically just
shuffles all of the elements and then checks to see if they are in order.
The complexity is O((n+1)!)'''