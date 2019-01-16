# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        index_of_min = i

        for j in range(i+1, len(arr)):
            if arr[index_of_min] > arr[j]:
                index_of_min = j

        temp = arr[i]
        arr[i] = arr[index_of_min]
        arr[index_of_min] = temp

    return arr



print(selection_sort([4, 3, 0, 2, 9, -7, 8]))



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr