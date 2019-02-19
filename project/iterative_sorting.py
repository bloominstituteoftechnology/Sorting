# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while(j >= 0 and temp < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    complete = False
    while not complete:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i-1] = temp
                swapped = True
        if not swapped:
            complete = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
