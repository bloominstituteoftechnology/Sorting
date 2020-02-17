# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    index = 0
    while index < len(arr):
        min = index
        for i in range(index + 1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[index] = arr[index], arr[min]
        index += 1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=200):
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
    count = [0] * (maximum + 1)
    result = [0] * len(arr)

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) -1, -1, -1):
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return result
