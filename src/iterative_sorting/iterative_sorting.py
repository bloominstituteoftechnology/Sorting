# TO-DO: Complete the selection_sort() function below

# Selection Sort:
# Given a list, take the current element
# and exchange it with the smallest element on the right hand side of the current element
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_element = arr[i]
        smallest_index = i
        smallest_element = cur_element
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest_element:
                smallest_index = j
                smallest_element = arr[j]
        # TO-DO: swap
        arr[i] = smallest_element
        arr[smallest_index] = cur_element
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# EXTRA STRETCH: Insertion sort:
# Insertion Sort:
# Given a list take the current element and it at the appropriate position of the list,
# adjust the list every time you insert.
# It's similar to arranging the cards in a Card game
def insertion_sort(arr):
    for i in range(1, len(arr)):
        pointer = i
        while pointer >= 1:
            if arr[pointer] < arr[pointer - 1]:
                temp = arr[pointer]
                arr[pointer] = arr[pointer - 1]
                arr[pointer - 1] = temp
            pointer -= 1
    return arr