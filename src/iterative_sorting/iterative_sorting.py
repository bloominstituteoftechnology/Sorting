# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
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
def bubble_sort( arr ):
    swap_occured = True
    while swap_occured:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp
                    swap_occured = True
                else: 
                    swap_occured = False

numbers = [3, 66, 4, 55, 42, 6, 67, 33]

bubble_sort(numbers)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr