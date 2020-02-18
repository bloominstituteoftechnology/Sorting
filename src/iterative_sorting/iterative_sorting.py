# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        idx_min_val = arr.index(min(arr[smallest_index:]))
        min_val = min(arr[smallest_index:])
        cur_index_val = arr[i]
        min_val_count = arr.count(min_val)
        # TO-DO: swap
        if (idx_min_val >= smallest_index) and min_val_count == 1:
            arr.insert(smallest_index, min_val)
            arr.pop(smallest_index + 1)
            arr.insert(idx_min_val, cur_index_val)
            arr.pop(idx_min_val + 1)
            i += 1

    return arr


selection_sort([1, 2, 3, 4, 1, 1, 1, 4, 5])

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
