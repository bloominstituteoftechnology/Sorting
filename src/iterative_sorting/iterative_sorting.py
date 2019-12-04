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
            return arr

    # return arr

print(bubble_sort([2,4,5,1,8,5]))

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # V2
    for i in range(len(arr)):
        # Set minimum spot in array --> where you are going to swap to
        min_index = i
        
        # loop through unsorted array 
        for x in range(i+1, len(arr)):

            # conditional to swap with current min index
            if arr[min_index] > arr[x]:
                min_index = x
    
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    
    return arr


    # V1
    # # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc) 

    #     # TO-DO: swap


    # return arr

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr