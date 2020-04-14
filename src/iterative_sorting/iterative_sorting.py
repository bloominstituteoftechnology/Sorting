# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element (hint, can do in 3 loc - lines of code) 
        # First, I need to iterate through the elements that remain in the arr
        for x in range(smallest_index + 1, len(arr)):
            # Second, I need to check if the element is smaller than the currently smallest
            if arr[x] < arr[smallest_index]:
                # Third, if this statement is True, I will need to set the new index to be the smallest
                smallest_index = x
        # TO-DO: swap the arr
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    # Looping through each element in the array
    for i in range(len(arr) - 1):
        # Looping through the remaining elements
        for x in range(len(arr) - 1 - i):
            # comparing this current element to the one to the right, if larger than we swap places(indices)
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]

    return arr


# STRETCH: implement the Count Sort function below
'''

Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array. The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

'''

# Looking in the test_iterative.py, in arr4, the range is set to 200 so I will sed the max to 200

def count_sort( arr, maximum=200 ):
    # iterate over array
    for i in arr:
        # checking to see if there is a negative element in the array; if so, return the statement in the test file
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
    # setting everything to zero
    count = [0] * (maximum + 1)
    arr_set = [0] * len(arr)

    for i in arr:
        count[i] +=1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        arr_set[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return arr_set