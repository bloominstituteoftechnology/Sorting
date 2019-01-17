# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    for i in range(0, len(arr)):
        cur_val = arr[i]
        pos = i
        while pos > 0 and cur_val < arr[pos-1]:
            print(arr)
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
            pos -= 1

        arr[pos] = cur_val
    return arr


# print(insertion_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    x = len(arr)
    while x > 0:
        for i in range(1, x):
            print(arr)
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        x -= 1
    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(arr1)
# print("bubble sort", bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
