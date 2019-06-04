# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


def bubble_sort2(arr):
    swapping_occured = True

    while swapping_occured:
        swapping_occured = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swapping_occured = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
# Implementation based on https://www.youtube.com/watch?v=7zuGmKfUt7s
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return []

    for num in arr:
        if num < 0:
            return 'Error, negative numbers not allowed in Count Sort'

    if maximum == -1:
        maximum = max(arr)

    # Create a count list to hold occurance
    count_list = [0] * (maximum+1)

    # print(count_list)

    # Check and update the occurance
    for i in range(len(arr)):
        count_list[arr[i]] += 1

    # print(count_list)

    # Find relative position
    for i in range(0, len(count_list)-1):
        count_list[i+1] += count_list[i]

    # print(count_list)

    # Create output array with len same as input arr
    output = [None] * len(arr)

    for i in range(len(arr)):
        # Find element's value in arr
        value = arr[i]
        # Find value's index from count_list
        index = count_list[value]
        # Put value in output array based on index
        output[index-1] = value
        # Decrement the index in count_list
        count_list[value] -= 1

    return output
