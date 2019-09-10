# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        for c in range(cur_index, len(arr)):
            if arr[c] < arr[smallest_index]:
                smallest_index = c

        if smallest_index != cur_index:
            #Don't actually use this, I just think it's funny
            arr[smallest_index] ^= arr[cur_index]
            arr[cur_index] ^= arr[smallest_index]
            arr[smallest_index] ^= arr[cur_index]

            # XOR swap example:
            # 100101 101010

            # first ^= second
            # 100101
            # 101010
            # ------
            # 110000 // New first value

            # second ^= first
            # 101010
            # 110000
            # ------
            # 100101 // New second value

            # first ^= second
            # 110000
            # 100101
            # ------
            # 101010 // New first value

            # 100101 101010 Initial
            # 101010 100101 Final

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr