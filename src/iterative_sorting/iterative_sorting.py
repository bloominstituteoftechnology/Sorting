arr = [4, 7, 9, 2, 3, 1, 0, 10, 6, 8, 5]
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            comp_index = j
            if arr[smallest_index] > arr[comp_index]:
                smallest_index = comp_index
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


print(selection_sort(arr))

# # TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: compare numbers
        for j in range(cur_index, len(arr)-1):
            first_num = j
            second_num = j + 1
            if arr[first_num] > arr[second_num]:
                # TO-DO: swap
                temp = arr[first_num]
                arr[first_num] = arr[second_num]
                arr[second_num] = temp
    return arr


print(bubble_sort(arr))


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
