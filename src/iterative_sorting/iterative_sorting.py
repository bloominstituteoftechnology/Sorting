# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] >= arr[j]:
                # found new smallest thing!
                smallest_index = j
        
        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Bubble Sort function below
def bubble_sort( arr ):
    # 'swap_flag' = true

    # while a 'swap_flag' = true
        # 'swap_flag' resets to false

        # for each item in arr
            # compare to item on RHS
            # swap if LHS > RHS AND set 'swap_flag' to true

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr