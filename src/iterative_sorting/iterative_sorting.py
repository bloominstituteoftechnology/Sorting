# TO-DO: Complete the selection_sort() function below
arr = [6, 3, 9, 1, 3, 7, 2]
print(f'before iterative sort', arr)


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(smallest_index + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
        if cur_index != smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # TO-DO: swap
    return arr
print(f'after iterative sort', selection_sort(arr))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range (0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

print(f'bubble sort', bubble_sort(arr))