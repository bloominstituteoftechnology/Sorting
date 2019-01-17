# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # find the smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[cur_index]:
                smallest_index = j
        
        # swap
        temporary = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temporary
        
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):

    # index 0 is already sorted
    # start at index 1 and compare it to the previous index (index 0)
    for index in range(1, len(arr)):
        current_element = arr[index]
        current_index = index
        
        # If current index is not 0, and the current element is smaller than the element before it...
        while current_index >= 0 and current_element < arr[current_index - 1]:
            # Take the previous one and put it in the current spot
            arr[current_index] = arr[current_index - 1]
            
            # Get the index for the previous spot
            current_index = current_index - 1
        
        # Put the current element in the previous spot, which is now being held by the current_index variable
        arr[current_index] = current_element
        
    return arr


# STRETCH: implement the Bubble Sort function below
# Bubble sorting is repeatedly swapping the two adjacent elements if they are in the wrong order.
def bubble_sort(arr):
    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum =- 1):

    return arr
    