# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Set Variables
    start_value = None
    end_value = None

    while True:
        noSwap = True
        for i in range(len(arr) -1): # 5 checks with 6 items in array (protecting from out of bounds)
            print(i)

            # Set Start & End
            start_value = arr[i]
            # print(start_value)

            end_value = arr[i + 1]
            # print(end_value  )

            if end_value < start_value:
                noSwap = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
            print(arr)

        if noSwap == True:
            return False

    return arr
bubble_sort([1,6,9,3,10,4])

# # TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 

#         # TO-DO: swap


#     return arr

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr