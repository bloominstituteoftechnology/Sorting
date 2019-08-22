# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]



    print(arr)
    return arr

# selection_sort([5,7,9,55,2,4])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    run = True
    for index in range(len(arr)):
        for i in range(0, len(arr)-index-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

bubble_sort([5,7,9,55,2,4])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
