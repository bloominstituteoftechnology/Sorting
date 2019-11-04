# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # cur_num = arr[i]
        # smallest_num = cur_num
        # lowest_index = i
        # for j in range(i, len(arr)):
        #     if arr[j] < smallest_num:
        #         smallest_num = arr[j]
        #         lowest_index = j
        # arr[i], arr[lowest_index] = smallest_num, cur_num   
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # ready_to_test = True
    # while ready_to_test:
    #     ready_to_test = False
    #     for i in range(1, len(arr)):
    #         if arr[i] < arr[i-1]:
    #             arr[i], arr[i-1] = arr[i-1], arr[i]
    #             ready_to_test = True
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr