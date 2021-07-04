# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(arr) - 1):
            next_num = i + 1
            if arr[next_num] < arr[i]:
                swap = True
                temp = arr[i]
                arr[i] = arr[next_num]
                arr[next_num] = temp

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
# 	return arr
