# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        value_1 = arr[i]
        value_2 = arr[smallest_index]
        arr[i] = value_2
        arr[smallest_index] = value_1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        swaps = 0
        for i in range(len(arr) - 1):
            value_1 = arr[i]
            value_2 = arr[i+1]
            if arr[i+1] < arr[i]:
                arr[i] = value_2
                arr[i+1] = value_1
                swaps += 1
        if swaps == 0:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    count_array = []
    for elem in arr:
        if elem < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if elem > len(count_array):
            count_array += [0 for i in range(elem - len(count_array) + 2)]
        count_array[elem] += 1
    for i in range(1, len(count_array)):
        count_array[i] = count_array[i] + count_array[i-1]
    last_inserted = -1
    for i in range(len(count_array)):
        where_to_insert = count_array[i] - 1
        while where_to_insert > last_inserted:
            arr[where_to_insert] = i
            where_to_insert -= 1
        last_inserted = count_array[i] - 1
    return arr
