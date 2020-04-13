# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Bubble sort basically checks each index of the array with its immediate neighbor, and swap given some condition.
    # If any swapping occurred during all checks, we loop.
    swappedLastPass = True
    while swappedLastPass:
        swappedLastPass = False
        for index, element in enumerate(arr):
            if index < len(arr) - 1 and element > arr[index + 1]:
                temp = element
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
                swappedLastPass = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
