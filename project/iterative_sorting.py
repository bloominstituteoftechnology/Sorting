# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # return arr for length 0 or 1
    if len(arr) < 2:
        return arr

    # loop through elements starting from second element
    for i in range(1, len(arr)):
        cur_index = i
        temp = arr[cur_index]

        #
        while cur_index > 0 and temp < arr[cur_index - 1]:
            arr[cur_index] = arr[cur_index - 1]
            cur_index -= 1

        arr[cur_index] = temp

        print(arr)

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
