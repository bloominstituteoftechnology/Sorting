def selection_sort(arr):
    # loop through n-1 elements
    # what's happening here is we're setting the i index to loop through each element
    # if that element
    for i in range(0, len(arr) - 1):
        cur_index = i
        if cur_index < (len(arr) - 1):
            smallest_index = i
        # for the selection sorting, we have to think up another (sub) array
        # We'll consider that the sorted array
        for j in range(i+1, len(arr)):
            if arr[smallest_index]  > arr[j]:
                smallest_index = j
            else:
                pass
        # swapping element 'positions' within the array
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]     
    return arr

# another way of doing it below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         i = smallest_index
#         # we'll need to create a sub-array to populated with sorted elements
#         for j in range(smallest_index+1, len(arr)):
#             if arr[j] > arr[smallest_index]:
#                 smallest_index = j
#         arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
#         print(arr)
#     return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr