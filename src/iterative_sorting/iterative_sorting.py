# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #ASSUME CURRENT FIRST ITEM IS THE SMALLEST
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

          #Write a for loop that starts at the smallest index   
        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
           


        # TO-DO: swap
        #SWAP LOWEST UNSORTED WITH FIRST UNSORTED ELEMENT
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr
#WORKS BY REPEATEDLY SWAPPING ELEMENTS IF THEY ARE IN THE WRONG ORDER
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n =len(arr)
    #GO THROUGH ALL ELEMENTS IN THE ARRAY
    for i in range(n):
        #Check last I element
        for j in range(0, n-i-1):

            #Swap if the next element is greater
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr