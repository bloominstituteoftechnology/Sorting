# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        smallest_value = arr[i]
        for j in range(i + 1, len(arr)):
            if smallest_value > arr[j]:
                smallest_index = j
                smallest_value = arr[j]

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = \
            arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    no_changes = False
    while no_changes is False:
        no_changes = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                no_changes = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    count = [0] * len(arr)
    output = [0] * len(arr)

    # build histogram of array
    for i in range(len(arr)):
        count[arr[i]] += 1

    # build cumulative sum of histogram
    # starting at index 2
    for i in range(1, len(array)):
        count[i] = count[i] + count[i - 1]

    for i in range(len(arr), 0, -1):
        output[count[arr[i]]] = arr[i]
        count[arr[i]] -= 1

    return output
