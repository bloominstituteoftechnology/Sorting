# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    for end in range(len(arr) - 1, 0, -1):
        position_of_max = 0

        for start in range(position_of_max, end + 1):
            if arr[start] > arr[position_of_max]:
                position_of_max = start

        # Swap
        temp = arr[end]
        arr[end] = arr[position_of_max]
        arr[position_of_max] = temp
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr