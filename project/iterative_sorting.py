# Complete the selection_sort() function below in class with your instructor


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    for i in range(1, len(arr)):
        # cur_index = i
        while arr[i] < arr[i - 1]:
            temp = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = temp
            # cur_index -= 1
    return arr


print(insertion_sort([22, 55, 77, 44, 66, 88, 11, 33]))

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
