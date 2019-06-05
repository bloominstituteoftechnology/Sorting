# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        smallest_value = arr[i]
        for j in range(i + 1, len(arr)):
            if smallest_value > arr[j]:
                smallest_index = j
                smallest_value = arr[j]
        # swap items
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap is True:
        swap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # create lists of each array item
    count = [0] * len(arr)
    output = [0] * len(arr)
    for i in range(len(arr)):
        count[arr[i]] += 1

    # sum each item (like a histogram chart)
    # start at second item
    for i in range(1, len(arr)):
        count[i] = count[i] + count[i - 1]

        # _  step in reverse
        for i in range(len(arr), 0, -1):
            output[count[arr[i]]] = arr[i]
            count[arr[i]] -= 1

    return arr
