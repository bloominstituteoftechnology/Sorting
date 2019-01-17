# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        cur_value = arr[i]
        position = i

        while position > 0 and arr[position-1] > cur_value:
            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = cur_value

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr ):
    max_value = max(arr) if len(arr) > 0 else 0
    index_list = list(range(0, max_value+1))
    count_list = [0] * (max_value + 1)
    result = []

    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count_list[i] += 1

    for index, i in enumerate(count_list):
        for j in range(0, i):
            result.append(index_list[index])

    return result