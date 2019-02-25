# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through the entire array starting at 0 and ending at the length of the array
    for i in range(0, len(arr) -1):
        # keeps track of the current index
        current_index = i
        # keeps track of the current smallest number 
        current_minimum = current_index
        # loop through the array starting at the current index to the end of the array. We start at the current index because everything on the left hand side of the current index is already sorted
        for j in range(current_index, len(arr)):
            # checks to see if the item at index j is less than item at index of current_minimum
            if arr[j] < arr[current_minimum]:
                # If the item at j is less than the item at current_minimum, current_minimum will now be j
                current_minimum = j
        
        # After we go through the entire array we swap the item at current_minimum with the current_index
        arr[current_minimum], arr[current_index] = arr[current_index], arr[current_minimum]


    return arr

print(selection_sort([78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114]))


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(0, len(arr)):
        temp = arr[i]

        j = i - 1
        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp 


    return arr


print(insertion_sort([78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr