# By Ben Hakes

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range (cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # loop through n-1 elements
    a_swap_happened = True
    sorted_index = len(arr) -1

    while a_swap_happened:
        a_swap_happened = False
        print(arr)
        for i in range(0, sorted_index):

            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)
            if arr[i] > arr[i + 1]:
                # TO-DO: swap
                a_swap_happened = True
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
        
        sorted_index -= 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    

    return arr