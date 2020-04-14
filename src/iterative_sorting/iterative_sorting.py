"""
# Swap function 
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
"""

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):                                        #For all indices EXCEPT the last index
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)):                                      #Loop through elements on right-hand-side of current index and find the smallest element                                
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # TO-DO: swap
        if smallest_index != cur_index:                                     #Swap the element at current index with the smallest element found in above loop
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):                                                     #Loop through your array
    for i in range(0, len(arr) - 1):                                        
        for x in range(0, len(arr)-(i+1)):                                  #Compare each element to its neighbor / Ensure if no swaps performed, stop
            if arr[x] > arr[x+1]:                                           #If elements in wrong position (relative to each other, swap them)
                arr[x], arr[x+1] = arr[x+1], arr[x]                         
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    size = 0
    counts = []
    result = []
    ## Create counts array
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if arr[i] > size:
            size = arr[i]
    for j in range(0, size+1):
        counts.append(0)
        for k in range(0, len(arr)):
            if arr[k] == j:
                counts[j] = counts[j] + 1
    print(counts, "counts")
    ## Shift counts array by adding current index value to next index value as new current index
    for l in range(1, len(counts)):
        counts[l] = counts[l] + counts[l-1]
    print(counts, "shifted counts")
    ## Shift counts array over; cutting off the last element and prepending a 0 before all elements.
    counts = counts[:-1]
    counts.insert(0, 0)
    print(counts, "second shift, counts array complete!")
    result = [None] * len(arr)
    for m in range(0, len(arr)):
        for n in range(0, len(counts)):
            if arr[m] == counts[n]:
                result[n] = arr[m]
    print(result, "result")
    arr = result
    return arr