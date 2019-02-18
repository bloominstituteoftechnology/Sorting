# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # fins next smallest element after that element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # swap that with current element
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # For each element in the array, find the next smallest element and swap it
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