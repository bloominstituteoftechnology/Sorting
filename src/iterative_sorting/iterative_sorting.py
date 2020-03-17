# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below


# def bubble_sort(arr):
#     swap = False
#     if swap == True:
#         arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
#     for i in range(0, len(arr)-1):
#         cur_index = i
#         next_index = cur_index
#         # Create loop throughout next number to compare
#         for j in range(cur_index, len(arr)):
#             if arr[j] > arr[next_index]:
#                 next_index = j
#                 arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
#         # if curr index is greater than next index, swap
#         # then add 1 to current index

#         # else if it's not, add 1 to current index and continue to next step
#     return arr

def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
    return arr
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
