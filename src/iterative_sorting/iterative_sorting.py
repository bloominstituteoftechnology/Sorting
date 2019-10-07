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
        cur_num = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = cur_num


    print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    swap_occurred = True
    last_index = len(arr) - 1
    while swap_occurred == True:
        swap_occurred = False

        if last_index == 0:
            break

        for i in range(last_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_occurred = True

        last_index -= 1
    

    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr