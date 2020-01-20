arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for checkIndex in range(cur_index, len(arr)):
            if arr[checkIndex] < arr[smallest_index]:
                smallest_index = checkIndex
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        cur_index += 1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr)):
            if index == 0:
                continue
            if arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                swapped = True
    return arr


bubble_sort(arr1)
print(arr1)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
