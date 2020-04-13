# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j 

        # TO-DO: swap
        a = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = a
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    #While swap is True
    while swap is True:
        #Compare each element to its neighbor
        i = 0
        count = 0
        while i < (len(arr) - 1):
            
        #If elements in wrong position (relative to each other, swap them)
            if arr[i] > arr[i+1]:
                a = arr[i]
                b = arr[i+1]
                arr[i] = b
                arr[i+1] = a
                i += 1
                count += 1
            else:
                i += 1

    # If no swaps performed, stop.
        if count < 1:
            swap = False  
    # Else, go back to the element at index 0 and repeat step 1.
        else:
            swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) < 1:
        return arr
    
    maximum = max(arr)
    
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    
    count = [0 * i for i in range(maximum + 1)]
 
    for x in arr:
        count[x] += 1   
   
    for i in range(len(count) - 1):
        count[i+1] = count[i+1] + count[i]
  
    for i in range(len(count)):
        count[i] -= 1
    
    final = [0 * i for i in range(len(arr))]
   
    for x in arr:
        fin_index = count[x]
        count[x] -= 1
        final[fin_index] = x
    
    return final