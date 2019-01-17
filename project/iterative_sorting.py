# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                min = arr[j];
                arr[j] = arr[i];
                arr[i] = min;

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        while i > 0 and arr[i - 1] > current:
            arr[i] = arr[i - 1]
            i = i - 1
            arr[i] = current

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr