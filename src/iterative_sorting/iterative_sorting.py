# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for num in range(i + 1, len(arr)):
            if arr[num] < arr[smallest_index]:
                smallest_index = num
        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    # loop through n-i elements

    for i in range(len(arr)):
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]

    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
