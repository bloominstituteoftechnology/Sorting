# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[smallest_index]
        # take the item at the current i, move it to where smallest item was
        arr[smallest_index] = arr[cur_index]
        # take smallest item put at current index
        arr[cur_index] = temp

    return arr


# implement the Insertion Sort function below
def insertion_sort(arr):
    # After first index
    for i in range(1, len(arr)):
        temp = arr[i]
        # iterate to left
        for j in range(len(arr[:i]), -1, -1):
            if temp < arr[j]:
                # slide item over ->
                arr[j+1] = arr[j]
                # insert temp at index
                arr[j] = temp

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
