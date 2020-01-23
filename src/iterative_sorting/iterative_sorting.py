# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for index in range(cur_index, len(arr)):
            if arr[index] < arr[smallest_index]:
                smallest_index = index

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for num in range(len(arr) - 1, 0, -1):
        for index in range(num):
            if arr[index] > arr[index + 1]:
                swap = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = swap
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#     return arr
