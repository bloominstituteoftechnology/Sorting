# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            else:
                pass

        # TO-DO: swap
        cur_val = arr[cur_index]
        smallest_val = arr[smallest_index]
        arr[cur_index] = smallest_val
        arr[smallest_index] = cur_val


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    counter = 1
    woof = "dog" # when swapped is false after complete run though
                    # stop the while loop
    while counter < len(arr):
        for i in range(0, len(arr) - counter):
            swapped = False
            i_val = arr[i]
            next_val = arr[i+1]
            
            if i_val > next_val:
                arr[i] = next_val
                arr[i+1] = i_val
            else:
                pass
        counter += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr