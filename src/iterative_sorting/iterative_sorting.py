# TO-DO: Complete the selection_sort() function below
#
import random

array1 = [3, 5, 1, 2, 4, 11, 9, 29, 23, 4]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        min_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        # TO-DO: swap

    return arr


print(selection_sort(array1))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(array1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
