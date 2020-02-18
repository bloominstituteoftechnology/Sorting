# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(1, len(arr)): # For all other indices, beginning with [1]:
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        temp = arr[cur_index]# Copy the item at that index into a temp variable
        while smallest_index > 0 and temp < arr[smallest_index-1]:
            print(smallest_index)
            # Swap minimum with first element
            arr[smallest_index] = arr[smallest_index - 1] # Iterate to the left until you 
            # find the correct index in the "sorted" part of the array at which this element should be inserted
            smallest_index -= 1
        arr[smallest_index] = temp # When the correct index is found, copy temp into this position
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n): # Loop through your array
        for j in range(0, n-i-1): # Compare each element to its neighbor
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # If elements in wrong position (relative to each other, swap them)
    return arr # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


# STRETCH: implement the Count Sort function below
def count_sort( arr ):
    output = [0 for i in range(maximum)]
    count = [0 for i in range(maximum)]
    arr = ["" for _ in arr]
    for i in arr:
        count[ord(i)] += 1

    for i in range(maximum):
        count[i] += count[i-1] # For all indices EXCEPT the last index:

    # Loop through elements on right-hand-side 
    # of current index and find the smallest element
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Swap the element at current index with the
    # smallest element found in above loop
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr