# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    for end in range(len(arr) - 1, 0, -1):
        max = 0
        for current_item in rang(max, end + 1):
            if arr[current_item] > arr[max]:
                max = current_item

        # going to look at doing this swap in a more Python fashion, this feels like I've done it in JS
        temp = arr[end]
        arr[end] = arr[max]
        arr[max] = temp
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i
        # this moves the existing items to the right so that the value can be inserted at the proper location
        while pos > 0 and arr[pos - 1] current:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = curr
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr