# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # progress through array looking for smaller number
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below

# UNDERSTAND
    # Compare consecutive items
    # The highest number will bubble all the way to the right with each iteration


def bubble_sort(arr):
    # PLAN
    #  create first iteration that takes in the first index
    for i in range(1, len(arr)):
        #  make another iteration that is always at the prev number
        for j in range(0, len(arr) - 1):
            #  if 2nd number is greater than the first, swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # i += 1
    return arr


a = [8, 2, 5, 1]
bubble_sort(a)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
