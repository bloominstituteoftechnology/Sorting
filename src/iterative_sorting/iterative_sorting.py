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

        temp_var = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_var



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    go_again = True
    while go_again == True:
        go_again = False
        for i in range(0, len(arr) - 1):
            cur_index = i
            neighbor = cur_index + 1

            if arr[cur_index] > arr[neighbor]:
                print(arr[cur_index], "is greater than", arr[neighbor])
                temp_var = arr[neighbor]
                arr[neighbor] = arr[cur_index]
                arr[cur_index] = temp_var
                go_again = True
            else:
                print(arr[cur_index], "is lesss than", arr[neighbor])




    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr