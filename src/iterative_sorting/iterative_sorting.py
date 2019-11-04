# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, (len(arr) - 1)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_ocur = True
    while swap_ocur is True:
        swap_ocur = False
        for i in range(0, (len(arr) - 1)):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_ocur = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    #take a count of each array element
    #place into a array that has as many indexes as the max N in given arr
        #can make for loop to find largest element in given array, make that size of arr
    #add up array elements consecutively
    #create another count array
    return arr