# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Isolate the first index of each iteration
        # Check the remaining indexes to the right for a value
        # smaller than the value at the current index (index i)
        for j in range(i+1, len(arr)):
            # If the value at index j is smaller than the value
            # at index i, swap them
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Create reverse of arr index to iterate through
    # As the larger numbers bubble to the right,
    # The list of indexes to sort becomes smaller
    for n in range(len(arr)-1, 0, -1):
        # For each pair of values n and k:
        for k in range(n):
            # If the value on the left is larger than the value to its right:
            if arr[k] > arr[k+1]:
                # Swap the two values so the larger value is on the right
                arr[k], arr[k+1] = arr[k+1], arr[k]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
