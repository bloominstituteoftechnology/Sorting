# TODO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        lowest = i
        for j in (range(i+1, len(arr))):
            if (arr[j] < arr[lowest]):
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


print(bubble_sort([77, 222, 34, 56, 71]))
